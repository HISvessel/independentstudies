import cv2
import numpy as np

img = cv2.imread('pic-work-03.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh_1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

thresh_2 = cv2.adaptiveThreshold(gray, 255,
                                cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 11, 2)

cv2.imshow('Original', img)

while True:
    key = cv2.waitKey(0) & 0XFF

    if key == ord('f'):
        cv2.imshow('simple threshold', thresh_1)
    
    elif key == ord('s'):
        cv2.imshow('adaptive throeshold', thresh_2)
    
    elif key == ord('q'):
        break

cv2.destroyAllWindows()
