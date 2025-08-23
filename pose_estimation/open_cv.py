"""this function will serve as an introduction to opencv,
a framework designed for computer vision technologies. THis can
capture video and images, draw overlays and process frames. 

in the concept of pose estimation, which we will discuss soon, this
is good for capturing webcam, manipulating frames, render skeletal
overlays, amongst other things."""

import cv2

cap = cv2.videocapture(0) #opens the webcam
while True: #while the webcam is open
    ret, frame = cap.read() #reading of frames on an open camera
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    cv2.imshow('Gray Camera Feed', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Quit on 'q'
        break

cap.release()
cv2.destroyAllWindows()
