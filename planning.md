# Bird Watcher Project Planning Document

## Project Overview

**Project Name:** Bird Watcher  
**Description:** Raspberry Pi camera system that detects and counts birds at a bird feeder in real-time.

### Goals
- Detect and draw bounding boxes around birds
- Count the number of birds in each frame
- Provide live monitoring capabilities

## Requirements

### Functional Requirements
- Raspberry Pi camera positioned stably and aimed at the bird feeder
- Live video feed capture and streaming capability
- Object detection model that identifies birds in each frame
- Real-time bird counting functionality

### Non-Functional Requirements
- Real-time performance capability
- Compatible with consumer-grade electronics (Raspberry Pi)
- Optimized for resource-constrained environments

## Technical Specifications

**Programming Language:** Python  
**Frameworks/Libraries:** OpenCV, YOLO (object detection)  
**Database:** None  
**Hardware:** Raspberry Pi with camera module

## Testing Results

### Test 1: Raspberry Pi OS with GUI
**Setup:** 1280x1280 frames scaled to 320x320 for YOLO processing  
**Performance:**
```
0: 640x640 2 dogs, 2 chairs, 1 bed, 1567.8ms
Speed: 22.2ms preprocess, 1567.8ms inference, 8.3ms postprocess per image at shape (1, 3, 640, 640)
```
**Results:** ~1.5 seconds per frame processing time  
**Observations:** System detected birds intermittently. Camera positioning and background of photo is critical.

### Test 2: Raspberry Pi OS Lite (No GUI)
**Setup:** Using lite version of Picamera2 and Raspberry Pi OS Lite  
**Performance:**
```
0: 640x640 1 chair, 1 potted plant, 1 tv, 1569.4ms
Speed: 11.0ms preprocess, 1569.4ms inference, 6.9ms postprocess per image at shape (1, 3, 640, 640)
```
**Results:** Minimal performance improvement despite GUI removal  
**Conclusion:** Raspberry Pi hardware limitations are the primary bottleneck

### Test 3: External Processing
**Setup:** Stream frames to more powerful hardware for inference  
**Performance:**
```
0: 640x640 1 toilet, 35.2ms
Speed: 1.2ms preprocess, 35.2ms inference, 0.5ms postprocess per image at shape (1, 3, 640, 640)
```
**Results:** Huge performance improvement, getting nearly 30 frames per second.(~40x faster)  

## Next Steps

1. **Camera positioning:**
   - Find best angle, distance, and autofocus distance
   - Minimize background complexity (?)

2. **Fine-tune detection parameters:**
   - Adjust confidence thresholds for bird detection
   - Test different models
   - Consider training custom model on bird feeder imagery

