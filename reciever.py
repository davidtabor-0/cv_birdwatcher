# Run this script on the computer where you want to perform the inferenece.
import cv2
import numpy as np
from ultralytics import YOLO

PI_IP = "192.168.1.220"
STREAM_URL = f"http://{PI_IP}:5000/video_feed"

model = YOLO('yolov8n.pt')

def process_stream():
    cap = cv2.VideoCapture(STREAM_URL)
    
    if not cap.isOpened():
        print(f"Error: Could not open stream at {STREAM_URL}")
        print("Make sure your Raspberry Pi is running and accessible")
        return
    
    print(f"Connected to stream at {STREAM_URL}")
    
    try:
        while True:
            ret, frame = cap.read()
            
            if not ret:
                print("Failed to read frame")
                break
            
            results = model(frame)
            
            for result in results:
                boxes = result.boxes
                if boxes is not None:
                    for box in boxes:
                        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                        confidence = box.conf[0].cpu().numpy()
                        class_id = int(box.cls[0].cpu().numpy())
                        
                        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                        cv2.putText(frame, f'Class {class_id}: {confidence:.2f}', 
                                   (int(x1), int(y1-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            cv2.imshow('YOLO Detection', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    except KeyboardInterrupt:
        print("Stream interrupted by user")
    
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    process_stream()