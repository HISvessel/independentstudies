import cv2


cap = cv2.VideoCapture('http://192.168.0.29:4747/video')
while True:
    success, frame = cap.read()
    if not success:
        print('Could not find source. Try again later')
        break
    
    keypoints, descritors = cv2.ORB_create().detectAndCompute(frame, None)
    keyframes = cv2.drawKeypoints(frame, keypoints,  None, color=(255, 0, 0), flags=0)

    rotated_keyframes = cv2.rotate(cv2.flip(keyframes, 1), cv2.ROTATE_90_CLOCKWISE)
    mirrored_frames = cv2.flip(rotated_keyframes, 1)
    cv2.imshow('Video Window with orbs', mirrored_frames)
    key = cv2.waitKey(1)
    if key & 0XFF == ord('s'):
        cv2.imwrite('test_save.jpg', mirrored_frames)
    if key & 0XFF == ord('q'):
        print('Finishing process')
        break

cap.release()
cv2.destroyAllWindows()