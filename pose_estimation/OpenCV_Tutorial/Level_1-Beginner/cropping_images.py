"""this script recieves an image and crops it"""


import cv2

img = cv2.imread("single-line.jpg")

#this crops an image by slicing the pixel's array to the desired
#pixel indeces
cropped = img[50:200, 100:300]

cv2.imshow("Original", img)

#runs a process that maps keyboard to perform cropping and quitting
while True:
    key = cv2.waitKey(0) & 0XFF

    #if c is pressed on the keyboard, then show the image
    #this process is run once, so no extra images pop into the screen if I re-press it by accident
    if key ==  ord('c'):
        cv2.imshow("Cropped", cropped)
        cv2.imshow('Second cropped', cropped)

    #if q is pressed on the keyboard, end the loop
    elif key == ord('q'):
        break

cv2.destroyAllWindows()
