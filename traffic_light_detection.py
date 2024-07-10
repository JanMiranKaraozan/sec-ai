import cv2
import numpy as np
import os

# Bulunduğunuz dizinin yolunu alın
current_dir = os.path.dirname(os.path.abspath(__file__))

# Haar cascade dosyasının yolu
cascade_path = os.path.join(current_dir, 'haarcascades', 'traffic_light.xml')

# Cascade sınıflandırıcısını yükle
traffic_light_cascade = cv2.CascadeClassifier(cascade_path)

def detect_traffic_lights_frame(frame):
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect traffic lights
    traffic_lights = traffic_light_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    # Convert frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define colors in HSV space for detection
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([179, 255, 255])
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    lower_green = np.array([50, 100, 100])
    upper_green = np.array([70, 255, 255])
    
    # Process each traffic light
    for (x, y, w, h) in traffic_lights:
        roi = hsv[y:y+h, x:x+w]  # Region of interest for traffic light
        
        # Mask for red color
        mask_red1 = cv2.inRange(roi, lower_red1, upper_red1)
        mask_red2 = cv2.inRange(roi, lower_red2, upper_red2)
        mask_red = cv2.bitwise_or(mask_red1, mask_red2)
        
        # Mask for yellow color
        mask_yellow = cv2.inRange(roi, lower_yellow, upper_yellow)
        
        # Mask for green color
        mask_green = cv2.inRange(roi, lower_green, upper_green)
        
        # Determine color by finding the maximum area of each mask
        color = "Unknown"
        for mask, col in zip([mask_red, mask_yellow, mask_green], ["Red", "Yellow", "Green"]):
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours:
                max_contour = max(contours, key=cv2.contourArea)
                area = cv2.contourArea(max_contour)
                if area > 50:  # Minimum area threshold for detection
                    color = col
                    break
        
        # Draw rectangle and label only if color is known
        if color in ["Red", "Yellow", "Green"]:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(frame, color, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    return frame

def main():
    """
    Main function to capture video from default camera and detect traffic lights.
    """
    cap = cv2.VideoCapture(0)  # Open default camera
    
    while True:
        ret, frame = cap.read()  # Read frame
        if not ret:
            print("Error: Could not read frame.")
            break
        
        frame = detect_traffic_lights_frame(frame)  # Detect traffic lights in frame
        
        cv2.imshow('Traffic Light Detection', frame)  # Display frame with traffic lights detected
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
