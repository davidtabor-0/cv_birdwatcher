import cv2
from picamera2 import Picamera2
from libcamera import controls

# Initialize the camera
picam2 = Picamera2()
picam2.preview_configuration.main.size = (1280, 720)
picam2.preview_configuration.main.format = 'RGB888'
picam2.preview_configuration.align()
picam2.configure('preview')
picam2.start()

# Iterate through focal lengths 1 to 10
for focal_length in range(1, 11):
    # Set the focal length
    picam2.set_controls({'AfMode': controls.AfModeEnum.Manual, 'LensPosition': float(focal_length)})
    
    cv2.waitKey(500)  # 500ms delay to stabilize focus
    
    # Capture frame
    frame = picam2.capture_array()
    
    # Display frame
    cv2.imshow('Camera', frame)
    
    filename = f'capture_focal_{focal_length}.jpg'
    cv2.imwrite(filename, frame)
    print(f'Saved image: {filename}')
    

# Cleanup
picam2.stop()
cv2.destroyAllWindows()
