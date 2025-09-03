import cv2 as cv
import numpy as np
import os

single_line_img = "single-line.jpg"
if not os.path.exists(single_line_img):
    raise FileNotFoundError("Incorrect path")

img = cv.imread(single_line_img)
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv.getAffineTransform(pts1, pts2)
warped = cv.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv.imshow("Control Group", img)
cv.imshow("Warped Image", warped)

cv.waitKey(0)
cv.destroyAllWindows()