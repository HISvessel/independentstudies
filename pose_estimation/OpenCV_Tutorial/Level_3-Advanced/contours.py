import cv2
import numpy as np

img = cv2.imread('pic-work-03.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#creates a binary format of the image, where the background
#is made of 0s and objects are made of 1s
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

#finds contours in the threshold image(the 1s)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    #draws contours on the original image(frame by frame)
    cv2.drawContours(img, [cnt], -1, (255, 255, 0), 2)

    #finds the area and perimeter of every contour pixel
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)

    #approximates contours to the polygon(based off area and perimeter)
    approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
    cv2.drawContours(img, [approx], -1, (255, 0, 255), 2)

    #finds the borders of the contours bounding box
    x, y, w, h = cv2.boundingRect(cnt)

    #draws a retangle around the contours based on the contour dimensions
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
