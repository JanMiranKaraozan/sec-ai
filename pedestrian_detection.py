import cv2

# lane_detection.py

def main():
    # Lane detection işlemleri burada yapılacak
    print("Lane detection işlemi başlatıldı.")
    # Lane detection kodları buraya gelecek

# Eğer bu script dosyası doğrudan çalıştırılıyorsa:
if __name__ == "__main__":
    main()

# Load pedestrian cascade
pedestrian_cascade = cv2.CascadeClassifier('haarcascades/pedestrian.xml')

def detect_pedestrians_frame(frame):
    """
    Detect pedestrians in a frame and draw rectangles around them.
    
    Args:
        frame (numpy array): The input frame.
    
    Returns:
        numpy array: The output frame with pedestrians detected and labeled.
    """
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect pedestrians
    pedestrians = pedestrian_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=2)
    
    # Draw rectangles around pedestrians
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 210), 4)
    
    return frame

def main():
    """
    Main function to capture video from default camera and detect pedestrians.
    """
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    while True:
        ret, frame = cap.read()  # Read frame from camera
        if not ret:
            print("Error: Could not read frame.")
            break
        
        frame = detect_pedestrians_frame(frame)  # Detect pedestrians in frame
        
        cv2.imshow('Pedestrian Detection', frame)  # Display frame with pedestrians detected
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
