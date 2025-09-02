"""this is part 2 and a followup script of OpenCV tutorial. This ime, we got
a practical example to apply. This module intends to employ webcam face detection."""

import cv2

# Load pre-trained face detector
CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
CASCADE_PROFILE = cv2.data.haarcascades + "haarcascade_profileface.xml"
face_cascade = cv2.CascadeClassifier(CASCADE_PATH)
profile_cascade = cv2.CascadeClassifier(CASCADE_PROFILE)

# Open webcam
cap = cv2.VideoCapture("http://192.168.0.15:4747/video") #set to WiFI IP address
while True:
    ret, frame = cap.read()  # Capture frame
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100,100))
    profiles = profile_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
    
    for (w, y, w, h) in profiles:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 1)

    cv2.imshow("Webcam Face Detection", frame)
    # Break on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()