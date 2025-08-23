"""this is part 2 and a followup script of OpenCV tutorial. This ime, we got
a practical example to apply. This module intends to employ webcam face detection."""

import cv2

# Load pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Open webcam
# the webcam is tied to a telephone via DroidCam
#vchanges are pending, so that a phone will not be used for the final
# project
cap = cv2.VideoCapture("http://192.168.0.15:4747/video")

while True:
    ret, frame = cap.read()  # Capture frame
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around detected faces
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

    cv2.imshow("Webcam Face Detection", frame)

    # Break on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()