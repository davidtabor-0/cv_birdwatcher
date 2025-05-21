# Project Planning Document

## Project Overview
- **Project Name**: Bird Watcher
- **Description**: Rasperry Pi camera detects the number of birds at a bird feeder live.
- **Goals**: 
    - Detect and draw bounding boxes around birds
    - Detect number of birds in a photo

## Requirements
### Functional Requirements
- The raspberry pi camera can sit in a stable position aimed at the feeder
- Live video feed can be captured
- Object detection model identifies birds in each frame
- Count number birds

### Non-Functional Requirements
- The program should run in real time
- The program should run on consumer grade electronics

## Technical Details
- **Programming Languages**: Python 
- **Frameworks/Libraries**: OpenCV,
- **Database**: None

## Milestones and Timeline
| Milestone         | Description                | Deadline       |
|-------------------|----------------------------|----------------|
|                   |                            |                |
|                   |                            |                |

## Notes
Output from first test: (relevant photos is dog_test) \
0: 640x640 2 dogs, 2 chairs, 1 bed, 1567.8ms \
Speed: 22.2ms preprocess, 1567.8ms inference, 8.3ms postprocess per image at shape (1, 3, 640, 640) \

Took a little over 1.5 seconds to generate a single frame. This was using the raspberry pi os with GUI. \
The frames are being taken in 1280x1280 and scaled down to 320x320 before being passed into yolo. \

I tested the system on the birdfeeder outside of our window. It does okay, it was detecting the birds sometimes. I think positioning the camera is key.

The next thing to do is run it on a fresh OS without GUI or preview and see if it does much better.

Output from second test:
0: 640x640 1 chair, 1 potted plant, 1 tv, 1569.4ms \
Speed: 11.0ms preprocess, 1569.4ms inference, 6.9ms postprocess per image at shape (1, 3, 640, 640) \
We see little improvement using the lite version of Picamera2 and Raspberry PI OS Lite