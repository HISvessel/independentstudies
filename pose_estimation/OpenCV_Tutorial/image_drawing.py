"""this module has several functions that allow us to make
drawings unto images. We can use the cv module to draw different geometric shapes

We can do so with these functions:
cv2.line()
cv2.circle()
cv2.rectangle()
cv2.ellipse()
cv2.putText()

our final product looks more like a computer generated picture that
we can load into the OpenCV module to display and save."""


import cv2 as cv
import numpy as np

#Lets start with a demo: draw a line inside of a black image
img = np.zeros((512, 512, 3), np.uint8)#an image made as an array of zeros of the given size

#this draws a diagonal blue line witha thickness of 5 pixels
cv.line(img, (0,0), (511, 511), (255,0,0), 5)

#we can now show the image
cv.imshow("Thick blue line", img)
key = cv.waitKey(0)
if key == ord("s"):
    cv.imwrite("single-line.jpg", img) #write the photo file into the system
cv.destroyAllWindows()