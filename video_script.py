from picamera2 import Picamera2
from ultralytics import YOLO
import cv2
import numpy as np

# Initialize the Raspberry Pi Camera
picam2 = Picamera2()
config = picam2.create_video_configuration(main={"size": (640, 480), "format": "RGB888"})
picam2.configure(config)
picam2.start()

# Load YOLOv8 nano
model = YOLO("yolov8n.pt")

# Video processing
try:
    while True:
        # Capture frame
        frame = picam2.capture_array()

        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Render results
        annotated_frame = results[0].plot()

        # Display frame with detections
        cv2.imshow("YOLOv8 Live Detection", annotated_frame)

        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    # Cleanup
    picam2.stop()
    cv2.destroyAllWindows()
