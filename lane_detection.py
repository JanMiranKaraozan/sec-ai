import cv2
import numpy as np

def detect_lanes(image):
    # Görüntüyü gri tonlamaya çevirme
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Gürültüyü azaltmak için Gaussian bulanıklığı uygulama
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Kenar tespiti için Canny kenar dedektörü uygulama
    edges = cv2.Canny(blur, 50, 150)
    
    # İlgili bir alan seçerek ROI (Region of Interest) belirleme
    height, width = image.shape[:2]
    mask = np.zeros_like(edges)
    polygon = np.array([[
        (0, height),
        (width // 2, height // 2 + 50),
        (width, height),
    ]], np.int32)
    cv2.fillPoly(mask, polygon, 255)
    masked_edges = cv2.bitwise_and(edges, mask)
    
    # Hough dönüşümü kullanarak şeritleri tespit etme
    lines = cv2.HoughLinesP(masked_edges, rho=1, theta=np.pi/180, threshold=20, minLineLength=20, maxLineGap=300)
    
    # Şeritler sınıflandırma
    left_lines = []
    right_lines = []
    
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            # Şeritlerin yönüne göre sol ve sağ şeritleri sınıflandırma
            if x2 != x1:
                slope = (y2 - y1) / (x2 - x1)
                if slope < -0.5:
                    left_lines.append(line[0])
                elif slope > 0.5:
                    right_lines.append(line[0])
    
    # Sol ve sağ şeritlerin orta noktalarını bulma
    left_lane, right_lane = average_slope_intercept(image, left_lines + right_lines)

    # Şeritler arasını çizme
    lane_image = np.zeros_like(image)
    if left_lane is not None and right_lane is not None:
        draw_lane_lines(lane_image, [left_lane, right_lane])
        
        # Şeritlerin arasını çizen çizgi
        middle_line = ((left_lane[2] + right_lane[2]) // 2, (left_lane[3] + right_lane[3]) // 2, 
                       (left_lane[0] + right_lane[0]) // 2, (left_lane[1] + right_lane[1]) // 2)
        cv2.line(lane_image, (middle_line[0], middle_line[1]), (middle_line[2], middle_line[3]), (0, 255, 0), 5)
    
    # Orijinal görüntü ile tespit edilen şeritleri birleştirme
    result = cv2.addWeighted(image, 0.8, lane_image, 1, 0)
    
    return result

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    
    for line in lines:
        x1, y1, x2, y2 = line
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    
    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    
    if len(left_fit) > 0 and len(right_fit) > 0:
        left_line = make_points(image, left_fit_average)
        right_line = make_points(image, right_fit_average)
        return left_line, right_line
    else:
        return None, None

def make_points(image, line_params):
    slope, intercept = line_params
    
    y1 = image.shape[0]
    y2 = int(y1 * (3 / 5))
    
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    
    return [x1, y1, x2, y2]

def draw_lane_lines(image, lines):
    if lines is not None:
        for line in lines:
            if line is not None:  # None kontrolü eklendi
                x1, y1, x2, y2 = line
                cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)

# Video akışından şerit tanıma
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    detected_lanes = detect_lanes(frame)
    
    cv2.imshow('Lane Detection', detected_lanes)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
