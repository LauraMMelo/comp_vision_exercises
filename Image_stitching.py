'''
Baseado no exemplo disponível em: https://www.pyimagesearch.com/2018/12/17/image-stitching-with-opencv-and-python/
'''

import cv2 as cv
from tkinter import *
from tkinter.filedialog import askopenfilenames
 
root = Tk()
root.withdraw()
imagePaths = askopenfilenames(initialdir = "./",title = "Select images to stitch",filetypes = (("jpg files","*.jpg"),("all files","*.*")))
print (imagePaths)
root.destroy()

images = []
for imagePath in imagePaths:
	image = cv.imread(imagePath)
	images.append(image)


print("stitching...")
stitcher = cv.Stitcher_create() 
(_, stitched) = stitcher.stitch(images)

cv.imwrite("output.png", stitched)
cv.imshow("Stitched", stitched)
cv.waitKey(0)
 