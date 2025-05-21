from picamera2 import Picamera2
import time
import cv2
from libcamera import controls
app = Flask(__name__)

# Initialize the camera
picam2 = Picamera2()
camera_config = picam2.create_video_configuration(main={"size": (720, 720)})
picam2.configure(camera_config)
picam2.set_controls({'AfMode': controls.AfModeEnum.Manual, 'LensPosition': 4.0})

def generate_frames():
    picam2.start()
    try:
        while True:
            # Capture frame as JPEG
            frame = picam2.capture_array()
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert from RGB >
            _, buffer = cv2.imencode('.jpg', frame)
            # Convert to JPEG
            frame = buffer.tobytes()
            
            # Yield frame in MJPEG format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            
            # Small delay to control frame rate
            time.sleep(0.033)  # ~30 FPS
    finally:
        picam2.stop()

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Raspberry Pi Camera Stream</title>
    </head>
    <body>
        <h1>Raspberry Pi Camera Stream</h1>
        <img src="/video_feed" style="max-width:100%;">
    </body>
    </html>
    '''

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Start Flask server on port 5000
    app.run(host='0.0.0.0', port=5000, threaded=True)