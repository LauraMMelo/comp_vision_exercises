import numpy as np
import argparse
import imutils
import time
import cv2
import os
import glob
# from tkinter import *
# from tkinter.filedialog import askopenfilename

args = { "input": 'filename',
         "output": "./static/output/output.avi",
         "yolo": "yolo-tiny",
         "confidence": 0.5,
         "threshold": 0.3
         }


labelsPath = os.path.sep.join([args["yolo"], "coco.names"])
LABELS = open(labelsPath).read().strip().split("\n")

np.random.seed(42)
COLORS = np.random.uniform(0, 255, size=(len(LABELS), 3))

# derive the paths to the YOLO weights and model configuration
weightsPath = os.path.sep.join([args["yolo"], "yolov3-tiny.weights"])
configPath = os.path.sep.join([args["yolo"], "yolov3-tiny.cfg"])
print("[INFO] loading YOLO from disk...")
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]


vs = cv2.VideoCapture(0)
writer = None
(W, H) = (None, None)

frameIndex = 0

start = time.time()
# loop over frames from the webcam stream
i = 0
while True:
	(grabbed, frame) = vs.read()

	if not grabbed:
		break
	
	if W is None or H is None:
		(H, W) = frame.shape[:2]

	blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
		swapRB=True, crop=False)
	net.setInput(blob)
	layerOutputs = net.forward(ln)
	

	# loop over each of the layer outputs
	for output in layerOutputs:
		# loop over each of the detections
		for detection in output:
			# extract the class ID and confidence (i.e., probability)
			# of the current object detection
			scores = detection[5:]
			classID = np.argmax(scores)
			confidence = scores[classID]

			if confidence > args["confidence"]:
				box = detection[0:4] * np.array([W, H, W, H])
				(centerX, centerY, width, height) = box.astype("int")

				# use the center (x, y)-coordinates to derive the top
				# and and left corner of the bounding box
				x = int(centerX - (width / 2))
				y = int(centerY - (height / 2))				

				label = "{}: {:.2f}%".format(LABELS[classID], confidence * 100)
				print("[INFO] {}".format(label))
				cv2.rectangle(frame, (x, y), (x+int(width), y+int(height)), COLORS[classID], 2)

	cv2.imshow("frame", frame)
	k = cv2.waitKey(1) & 0xff
	if k == ord("c"):
		break

	i+=1

end = time.time()
print("[INFO] script ran for {} seconds".format(end-start))
print("[INFO] {} frames were processed".format(i))
print("[INFO] Frames per seconds: {} ".format(i/(end-start)))

