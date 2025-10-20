import mediapipe as mp
import numpy as np
import cv2
from form_analysis import FormAnalyzer
from mediapipe.framework.formats import landmark_pb2

cap = cv2.VideoCapture('http://192.168.0.8:4747/video')
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

pose = mp_pose.Pose()

if not cap.isOpened():
    print('Cannot open camera, there is no feed to take')

#creating our own frozenset of body connections for drawing utils
body_connections = frozenset([  (11, 12), (11, 13), (13, 15), (12, 14), (14, 16),
                                  (11, 23), (12, 24), (11, 24), (12, 23), (23, 24),
                                  (23, 25), (24, 26), (25, 27), (26, 28)])

body_landmarks = [
    mp_pose.PoseLandmark.LEFT_SHOULDER.value,
    mp_pose.PoseLandmark.RIGHT_SHOULDER.value,
    mp_pose.PoseLandmark.LEFT_ELBOW.value,
    mp_pose.PoseLandmark.RIGHT_ELBOW.value,
    mp_pose.PoseLandmark.LEFT_WRIST.value,
    mp_pose.PoseLandmark.RIGHT_WRIST.value,
    mp_pose.PoseLandmark.LEFT_HIP.value,
    mp_pose.PoseLandmark.RIGHT_HIP.value,
    mp_pose.PoseLandmark.LEFT_KNEE.value,
    mp_pose.PoseLandmark.RIGHT_KNEE.value,
    mp_pose.PoseLandmark.LEFT_ANKLE.value,
    mp_pose.PoseLandmark.RIGHT_ANKLE.value,
    mp_pose.PoseLandmark.LEFT_HEEL.value,
    mp_pose.PoseLandmark.RIGHT_HEEL.value
]
while True:
    success, frame = cap.read()

    if not success:
        print('Failure at reading.')
        break

    #converting to RBG format for Mediapipe
    pose_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    #creating our own frozenset of body connections for drawing utils
    #body_connections = frozenset([  (11, 12), (11, 13), (13, 15), (12, 14), (14, 16),
    #                              (11, 23), (12, 24), (11, 24), (12, 23), (23, 24),
    #                              (23, 25), (24, 26), (25, 27), (26, 28)])
    result = pose.process(pose_frame)

    #selecting our landmarks for math equation

    if result.pose_landmarks:
        custom_landmark_list = landmark_pb2.NormalizedLandmarkList()
        #custom_landmark_list.extend(body_landmarks)

        landmarks = result.pose_landmarks.landmark
        l_shoulder = landmarks[11]
        r_shoulder = landmarks[12]
        l_elbow = landmarks[13]
        l_wrist = landmarks[15]
        r_elbow = landmarks[14]
        r_wrist = landmarks[16]
        l_hip = landmarks[23]
        r_hip = landmarks[24]
        l_knee = landmarks[25]
        r_knee = landmarks[26]
        l_ankle = landmarks[27]
        r_ankle = landmarks[28]


        mp_draw.draw_landmarks(pose_frame,
                              result.pose_landmarks,
                              body_connections,
                              mp_draw.DrawingSpec((200, 150, 0), 2, 2),
                              mp_draw.DrawingSpec((112, 112, 112), 1, 2))

    #preparing our math equations for displaying form cues as text on windows
    arm_bending_form = FormAnalyzer.calculate_angle([l_shoulder.x, l_shoulder.y],
                                                    [l_elbow.x, l_elbow.y],
                                                    [l_wrist.x, l_wrist.y])
    
    body_straight_form = FormAnalyzer.calculate_angle([l_shoulder.x, l_shoulder.y],
                                                      [l_hip.x, l_hip.y],
                                                      [l_ankle.x, l_ankle.y])
    
    if arm_bending_form < 45:
        cv2.putText(pose_frame,
                    'Good, you have bent the arm correctly',
                    [50, 50],
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 180, 0), 2)
    
    if body_straight_form == 180:
        cv2.putText(pose_frame,
                    'Body is very straight!',
                    [50, 75],
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 180, 0), 2)

    if body_straight_form < 160:
        cv2.putText(pose_frame,
                    f'Sagging the hips down: {body_straight_form}. Engage core!',
                    [50, 100],
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (180, 0, 0), 2)
    
    if body_straight_form > 190:
        cv2.putText(pose_frame, 
                    'Piking at the hips. Tighten glutes!', 
                    [50, 150], 
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (180, 0, 0), 2)

    #converting back to BGR format and displaying on screen
    frames_with_landmarks = cv2.cvtColor(pose_frame, cv2.COLOR_RGB2BGR)
    cv2.imshow('Exercise page', frames_with_landmarks)
    key = cv2.waitKey(1) & 0XFF

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
