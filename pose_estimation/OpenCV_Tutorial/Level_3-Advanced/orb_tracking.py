import cv2


def orb_creation(pic):
    img = cv2.imread(pic)
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(img, None)
    kp_img = cv2.drawKeypoints(img, keypoints, None, color=(0, 255, 0), flags=0)
    return kp_img


kp_img = orb_creation('pic-work-03.jpg')
cv2.imshow('image with orbs', kp_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
