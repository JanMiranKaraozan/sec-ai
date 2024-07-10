import cv2
import os

# Bulunduğunuz dizinin yolunu alın
current_dir = os.path.dirname(os.path.abspath(__file__))

# Haar cascade dosyasının yolu
cascade_path = os.path.join(current_dir, 'haarcascades', 'vehicles.xml')

# Cascade sınıflandırıcısını yükle
car_cascade = cv2.CascadeClassifier(cascade_path)

def detect_vehicles_frame(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Histogram equalization for better contrast
    gray = cv2.equalizeHist(gray)
    
    # Detect vehicles
    vehicles = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around vehicles
    for (x, y, w, h) in vehicles:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    return frame

# Example usage for testing
if __name__ == '__main__':
    cap = cv2.VideoCapture(0)  # Open default camera
    while True:
        ret, frame = cap.read()  # Read frame
        if not ret:
            print("Error: Could not read frame.")
            break
        
        frame = detect_vehicles_frame(frame)  # Detect vehicles in frame
        
        cv2.imshow('Vehicle Detection', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()