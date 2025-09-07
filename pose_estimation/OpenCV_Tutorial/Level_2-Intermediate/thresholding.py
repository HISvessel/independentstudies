import cv2
import numpy as np

img = cv2.imread('pic-work-03.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh_1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

thresh_2 = cv2.adaptiveThreshold(gray, 255,
                                cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 11, 2)
#a 5x5 matrix of 1s in unsigned int8
kernel = np.ones((5, 5), np.uint8)

dilated = cv2.dilate(thresh_1, kernel, iterations=1)
eroded = cv2.erode(thresh_1, kernel, iterations=1)

print('Preparing pictures, please wait...')
cv2.imshow('Original', img)
print()
print('This is the original picture')
print('To see effects, press any of the following keys')
print('f for simple threshold')
print('s for adaptive threshold')
print('d to dilate the image')
print('e to arode the image')

while True:
    key = cv2.waitKey(0) & 0XFF

    if key == ord('f'):
        print()
        print('You have selected f')
        cv2.imshow('simple threshold', thresh_1)
        print('This is a simple thresholding process')
    
    elif key == ord('s'):
        print()
        print('You have selected s')
        cv2.imshow('adaptive throeshold', thresh_2)
        print('This threshold method is more adaptive')
    
    elif key == ord('d'):
        print()
        print('You have selected d')
        cv2.imshow('Dilated image', dilated)
        print('This image has been dilated')

    elif key == ord('e'):
        print()
        print('You have selected e')
        cv2.imshow('', eroded)
        print('This picture was eroded')

    elif key == ord('q'):
        print('You have selected q. Finishing process. Goodbye.')
        break

cv2.destroyAllWindows()
