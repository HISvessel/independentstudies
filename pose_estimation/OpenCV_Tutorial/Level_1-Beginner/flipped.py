"""this module explores flipping and rotating images"""

import cv2

img = cv2.imread("lena.jpg")

#flips images horizontal
mirrored_img = cv2.flip(img, 1)

#flips images vertically
inverted_img = cv2.flip(img, 0)

#flips images vertically and horizontally
mirror_inverted_img = cv2.flip(img, -1)

#rotated images in two styles

#simple rotate of an image
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
vertical, horizontal, _ = rotated.shape

center_x = horizontal // 2
center_y = vertical // 2

"""drawing a red reticle in the center of the camera shot"""
        #horizontal line of the frame reticle
cv2.line(rotated, (center_x + 10, center_y), (center_x - 10, center_y), (0, 0, 150), 2)
        
        #the vertical line of the frame reticle
cv2.line(rotated, (center_x, center_y + 10), (center_x, center_y - 10), (0, 0, 150), 2)

        #drawing a square arouund the reticle
cv2.rectangle(rotated, (center_x - 200, center_y + 200), (center_x + 200, center_y - 200), (0, 0, 150), 3)
#fine rotation of an image
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
matr = cv2.getRotationMatrix2D(center, 30, 1.0)
finely_rotated = cv2.warpAffine(img, matr, (w, h))

#cv2.imshow("Orignial", img)
#cv2.imshow("Horizonal flip", mirrored_img)
#cv2.imshow("Vertical flip", inverted_img)
#cv2.imshow("Total flip", mirror_inverted_img)
cv2.imshow("Rotated Clockwise", rotated)
#cv2.imshow("Finely Rotated", finely_rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()