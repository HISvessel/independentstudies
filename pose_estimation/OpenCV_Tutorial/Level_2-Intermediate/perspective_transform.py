import cv2 as cv
import numpy as np

img = cv.imread('pic-work-03.jpg')

pts1 = np.float32([[56,65], [368,52], [28,387], [389,390]])
pts2 = np.float32([[0,0], [300,0], [0,300], [300,300]])

M = cv.getPerspectiveTransform(pts1, pts2)
dst = cv.warpPerspective(img, M, (300, 300))

cv.imshow('original', img)
while True:
    key = cv.waitKey(0) & 0XFF
    if key == ord('w'):
        cv.imshow('warped img', dst)
    
    elif key == ord('q'):
        break

cv.destroyAllWindows()
