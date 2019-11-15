'''
Baseado no exemplo de Fluxo Óptico disponível no site do OpenCV: https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html
'''

import numpy as np
import cv2 as cv

lines = []
drawing = False
point1 = ()
point2 = ()
def mouse_drawing(event, x, y, flags, params):
	global point1, point2, drawing, frame
	if event == cv.EVENT_LBUTTONDOWN:
		if drawing is False:
			drawing = True
			point1 = (x, y)
		else:
			drawing = False
	elif event == cv.EVENT_MOUSEMOVE:
		frame = frame_copy.copy()
		if drawing is True:
			point2 = (x, y)


cap = cv.VideoCapture(0)

# vs = cv.VideoCapture(args["input"])
(grabbed, frame) = cap.read()

cv.namedWindow("Frame")
cv.setMouseCallback("Frame", mouse_drawing)

frame_copy = frame
count = 0
while(1):
    cv.imshow("Frame", frame)
    if point1 and point2:
        cv.rectangle(frame, point1, point2, (0, 255, 255), 1)
    k = cv.waitKey(1) & 0xFF
    if k == ord("c"):
        lines.append([point1, point2, count])
        break
    # if k == ord("l"):
    #     cv.rectangle(frame_copy, point1, point2, (0, 255, 0), 6)
    #     lines.append([point1, point2, count])
    #     point1 = ()
    #     point2 = ()
    #     drawing=False
cv.destroyAllWindows()

mask_shitomasi = np.zeros_like(frame)
mask_shitomasi = cv.cvtColor(mask_shitomasi, cv.COLOR_BGR2GRAY)
mask_shitomasi[lines[0][0][1]:lines[0][1][1],lines[0][0][0]:lines[0][1][0]] = 255
mask_shitomasi = cv.normalize(src=mask_shitomasi, dst=None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8UC1)

# cv.namedWindow("Frame")
# cv.imshow("Frame", mask_shitomasi)
# cv.waitKey(0)
# cv.destroyAllWindows()


# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 ,
                       mask = mask_shitomasi)


# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
# Create some random colors
color = np.random.randint(0,255,(100,3))


# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
p0 = cv.goodFeaturesToTrack(old_gray, **feature_params)


# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

while(1):
    # print(lines)
    ret,frame = cap.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # calculate optical flow
    p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    # Select good points
    good_new = p1[st==1]
    good_old = p0[st==1]
    # draw the tracks
    for i,(new,old) in enumerate(zip(good_new, good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv.line(mask, (a,b),(c,d), color[i].tolist(), 2)
        frame = cv.circle(frame,(a,b),5,color[i].tolist(),-1)
    img = cv.add(frame,mask)
    cv.rectangle(img, lines[0][0], lines[0][1], (0, 255, 255), 1)
    cv.imshow('frame',img)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)