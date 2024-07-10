import cv2
import os

# Define the path to the XML file for stop sign detection
CASCADE_FILE = os.path.join('haarcascades', 'stop_sign.xml')

# Load the trained cascade classifier for stop signs
stop_sign_cascade = cv2.CascadeClassifier(CASCADE_FILE)

# Function to detect stop signs in a frame
def detect_stop_signs_frame(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect stop signs
    stop_signs = stop_sign_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around stop signs
    for (x, y, w, h) in stop_signs:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)
        cv2.putText(frame, 'Stop Sign', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
    
    # Display frame with stop signs detected
    cv2.imshow('Stop Sign Detection', frame)

# Example usage for testing
if __name__ == '__main__':
    cap = cv2.VideoCapture(0)  # Open default camera
    while True:
        ret, frame = cap.read()  # Read frame
        if not ret:
            print("Error: Could not read frame.")
            break
        
        detect_stop_signs_frame(frame)  # Detect stop signs in frame
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
