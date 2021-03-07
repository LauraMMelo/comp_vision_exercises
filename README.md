# Computer Vision Exercises

Solutions for the computer vision tests

## 0) Dependencies
OpenCV -v=4.0.0 
tkinter -v=8.6


##  1) Optical flow and tracking

The script `Optical_flow.py` runs the Optical Fluck computation through the Lucas Kanade method. Steps:

1. In the terminal, on the root folder, run `python Optical flow.py`. The webcam will take a picture.
2. Use the mouse to mark a rectangle with the object to be traced. Click once to start, then once to finish
3. Press 'c'. The object will then bem traced.
4. Press Ctrl+c in the terminal to stop.

##  2) Image Stitching

The script `Image_stitching.py` does o stitching. Steps:

1. In the terminal, on the root folder, run `python Image_stitching.py`. 
2. Select in the window the images that you want to stitch and press Open.
3. The stitched image should appear in the screen and then get saved as `output.png`

##  3) Object Detection

The script `Object_detection.py` runs YOLOv3-tiny through the Deep Neural Network module from OpenCV. 
YOLO has a set of architectures available, all trained in the COCO Dataset trainval, with a performance up to
57.9 *mean average precision* for the YOLOv3-608, and of 60.6 for the YOLOv3-spp, in COCO Dataset test-dev,
both being able to run at 20 FPS in a Pascal Titan X GPU. Due to the limited resources of the computer 
where these examples were developed, YOLOv3-tiny was chosen.

A YOLOv3-tiny reaches a performance of 33.1 mAP and may run up to 220 FPS. The computer where this
scipt was developed managed to run at 4 FPS, and has the following settings:

- Intel Core i3-5005 @ 2GHz
- 12Gb RAM memory
- On-board GPU (Not used in this script script)


1. On terminal, in the root folder, run `python Object_detection.py`. A webcam window will appear. Try showing objects such as a phone or a mug in front of the camera
2. To finish, press 'c'. The terminal will then print a simple report with the FPS rate during the script runtime.

