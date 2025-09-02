"""this script recieves an image and crops it"""


import cv2

img = cv2.imread("single-line.jpg")

#this crops an image by slicing the pixel's array to the desired
#pixel indeces
cropped = img[50:200, 100:300]

cv2.imshow("Original", img)
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()