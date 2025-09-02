"""this module contains a script to learn resizing of images

images can be reiszed in two different methods, 

By pixel size: you can manually put the pixel size array into however
size you want it

By scale: the sizing scale can be made in a scale relative to the original
picture, you can set the X axis to half the size with fx=0.5 or the
vertical axis to half the original size with fy=0.5"""

import cv2

img = cv2.imread("single-line.jpg")
resized = cv2.resize(img, (300, 200))
resized_scale = cv2.resize(img, None, fx=0.5,fy=0.5)
cv2.imshow("Original", img)
cv2.imshow("Resized Image", resized)
cv2.imshow("Resized with scale", resized_scale)
cv2.waitKey(0)
cv2.destroyAllWindows()