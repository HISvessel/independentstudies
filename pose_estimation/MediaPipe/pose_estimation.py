"""this function is a test created by chatgpt to tutor me in pose estimation, opencv,
data compiling and camera functionality. if all goes accordingly, we should be able
to start a process to open a camera, record movement and close it. This is the first of 
many tests."""

import cv2
import mediapipe as mp

# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Start webcam
#Camera taken from iPhone sharing the same WiFi port as laptop
cap = cv2.VideoCapture("http://192.168.9.176:4747/video")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to RGB (MediaPipe requires RGB input)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame and detect pose
    results = pose.process(rgb_frame)

    # If landmarks are detected, draw them
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    # Display the output
    cv2.imshow("Pose Estimation", rotated_frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()