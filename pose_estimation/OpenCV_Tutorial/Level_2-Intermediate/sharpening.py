import cv2 as cv
import numpy as np

img = cv.imread('pic-work-03.jpg')

kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])

sharpened = cv.filter2D(img, -1, kernel)

print('Starting process.')
print('Press s to sharpen image')
print('Press q to quit')
print('Loading image...')
print()
cv.imshow('Original', img)
print()
print('This is the original image.')
while True:
    key = cv.waitKey(0) & 0XFF

    if key == ord('s'):
        cv.imshow('Sharpened image', sharpened)
        print('This is the sharpened image.')

    elif key == ord('q'):
        print('Finishing process. Goodbye.')
        break

cv.destroyAllWindows()