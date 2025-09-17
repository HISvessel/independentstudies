import cv2
import numpy as np
from orb_tracking import orb_creation

img = cv2.imread('pic-work-03.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, maxCorners=150, qualityLevel=0.01, minDistance=5)
corners = np.intp(corners)

corners_2 = cv2.goodFeaturesToTrack(gray, maxCorners=100, qualityLevel=0.01, minDistance=10)
corners_2 = np.intp(corners_2)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

for corner in corners_2:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

kp_img = orb_creation(img)
cv2.imshow('Detecting of corners', img)
cv2.imshow('Orb creation on Borders', kp_img)
cv2.waitKey(0)
cv2.destroyAllWindows()