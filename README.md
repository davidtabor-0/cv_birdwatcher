# Bird Watcher

A real-time bird detection and counting system using Raspberry Pi camera and YOLO object detection.

## Overview

This project uses a Raspberry Pi with camera to monitor a bird feeder and detect/count birds in real-time. Due to performance constraints on the Pi, the system uses a client-server architecture where the Pi captures video frames and streams them to a more powerful computer for YOLO inference processing.



## Setup

### Raspberry Pi (Client)
Run the stream.py script on the raspberry pi. Run reciever.py on the computer recieveing the video and performing inference.

## Requirements

### Raspberry Pi
- Python 3.7+
- OpenCV
- Picamera2
- Network connection

### Processing Computer
- Python 3.7+
- OpenCV
- YOLO model files
- Sufficient GPU/CPU for real-time inference

## Usage

1. Position Raspberry Pi camera aimed at bird feeder
2. Start detection server on processing computer
3. Start camera stream on Raspberry Pi
4. Monitor detection results and bird counts

