import mediapipe as mp
import numpy as np
import cv2
from form_analysis import FormAnalyzer

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
#
READY_FOR_PUSHUP = False
READY_FOR_SQUAT = False

#counter for our individual exercises
PUSHUP_COUNTER = 0
SQUAT_COUNTER = 0

#toggle selector of our frames to read
exercise_module = {
    0: 'default',
    1: 'pushup',
    2: 'squat'
}
#selecting a proxy element to iterate through on toggle
mode_selector = 1

#the final display to show
display = None


while True:
    success, frame = cap.read()
    if not success:
        print('Failure at reading.')
        break

    #selecting the default frames with no effects or visuals
    if mode_selector == 0:
        display = frame

    #selecting the pushup model and data
    elif mode_selector == 1:
        """RGB frames for portraint camera"""
        pose_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        """RGB frames for smartphone camera"""
        result = pose.process(pose_frame)
        if not result.pose_landmarks:
            continue

        landmarks = result.pose_landmarks.landmark
        #Manually selecting all of the desired pose landmarks to focus on for computation
        l_ear = landmarks[7]
        r_ear = landmarks[8]
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
        l_heel = landmarks[29]
        r_heel = landmarks[30]
        l_toe = landmarks[31]
        r_toe = landmarks[32]

        #optimizing arm bend for a 60 degrees bend rule
        left_arm_bending_form = FormAnalyzer.calculate_angle([l_shoulder.x, l_shoulder.y],
                                                    [l_elbow.x, l_elbow.y],
                                                    [l_wrist.x, l_wrist.y])

        right_arm_bending_form = FormAnalyzer.calculate_angle([l_shoulder.x, l_shoulder.y],
                                                    [l_elbow.x, l_elbow.y],
                                                    [l_wrist.x, l_wrist.y])

        #optimizing elbow flaring for a 30 degree bend(try for x*z and y*z)
        left_arm_flaring_form = FormAnalyzer.calculate_flare_angle([l_shoulder.x, l_shoulder.y],
                                                        [l_elbow.x, l_elbow.y],
                                                        [l_wrist.x, l_wrist.y])

        right_arm_flaring_form = FormAnalyzer.calculate_flare_angle([l_shoulder.x, l_shoulder.y],
                                                        [l_elbow.x, l_elbow.y],
                                                        [l_wrist.x, l_wrist.y])

        #optimizing leg straightness for a 160 degree bend rule
        leg_bending_form = FormAnalyzer.calculate_angle([l_hip.x, l_hip.y],
                                                    [l_knee.x, l_knee.y],
                                                    [l_toe.x, l_toe.y])

        body_straight_form = FormAnalyzer.calculate_body_angle([l_ear.y, l_ear.x],
                                                      [l_hip.y, l_hip.x],
                                                      [l_ankle.y, l_ankle.x])

        pushup_body_angle = FormAnalyzer.calculate_angle([l_wrist.y, l_wrist.x],
                                                         [l_hip.y, l_hip.x],
                                                         [l_ankle.y, l_ankle.x])
        pushup_position = 70 <= pushup_body_angle <= 90 and l_hip.y < l_heel.y
        if pushup_position:
            mp_draw.draw_landmarks(pose_frame,
                              result.pose_landmarks,
                              body_connections,
                              mp_draw.DrawingSpec((112, 112, 112), 3, 3),
                              mp_draw.DrawingSpec((50, 255, 25), 2, 2))
        
        if left_arm_flaring_form > 45:
            cv2.putText(pose_frame, 'Elbow flaring detected', [75, 50], cv2.FONT_HERSHEY_SIMPLEX, 0.7, (190, 0, 0))

        if right_arm_flaring_form > 45:
            cv2.putText(pose_frame, 'Elbow flaring detected', [75, 100], cv2.FONT_HERSHEY_SIMPLEX, 0.7, (190, 0, 0))

        # research text for arm bending coordinates
        cv2.putText(pose_frame, f'Left Arm bend angle: {left_arm_bending_form}', [900, 50], #[900, 50] for portait views, [50, 200] for phones
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 70, 190), 2, cv2.LINE_AA)

        #research text for elbow flaring coordinates
        cv2.putText(pose_frame, f'Left Elbow flare angle: {left_arm_flaring_form}', [900, 100], #[900, 50] for portait views, [50, 200] for phones
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 70, 190), 2, cv2.LINE_AA)
        
        #research text for elbow flaring coordinates
        cv2.putText(pose_frame, f'Current body angle: {pushup_body_angle}', [900, 150], #[900, 50] for portait views, [50, 200] for phones
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 70, 190), 2, cv2.LINE_AA)

        converted_pushup_display = cv2.cvtColor(pose_frame, cv2.COLOR_RGB2BGR)
        display = converted_pushup_display

    #selcting the squat model and data
    elif mode_selector == 2:

        """RGB frames for portraint camera"""
        pose_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
        """RGB frames for smartphone camera"""
        result = pose.process(pose_frame)

        if not result.pose_landmarks:
            continue

        landmarks = result.pose_landmarks.landmark
        #Manually selecting all of the desired pose landmarks to focus on for computation
        l_ear = landmarks[7]
        r_ear = landmarks[8]
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
        l_heel = landmarks[29]
        r_heel = landmarks[30]


        #preparing our math equations for displaying form cues as text on windows    
        leg_bending_form = FormAnalyzer.calculate_angle([l_hip.x, l_hip.y],
                                                    [l_knee.x, l_knee.y],
                                                    [l_heel.x, l_heel.y])
    
        body_straight_form = FormAnalyzer.calculate_body_angle([l_ear.y, l_ear.x],
                                                      [l_hip.y, l_hip.x],
                                                      [l_ankle.y, l_ankle.x])
    
        mp_draw.draw_landmarks(pose_frame,
                              result.pose_landmarks,
                              body_connections,
                              mp_draw.DrawingSpec((112, 112, 112), 3, 3),
                              mp_draw.DrawingSpec((50, 205, 25), 4, 4))

        if leg_bending_form < 60:
            cv2.putText(pose_frame,
                     'Leg is bending for a squat',
                     [50, 25], 
                     cv2.FONT_HERSHEY_SIMPLEX,
                     0.7, (0, 180, 0), 2)

        if 180 < body_straight_form < 190:
            cv2.putText(pose_frame,
                    'Body is straight!',
                    [50, 75],
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 180, 0), 2)

        if body_straight_form < 160 and leg_bending_form < 60:
            cv2.putText(pose_frame,
                    f"That's a squat",
                    [50, 100],
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (180, 0, 0), 2)

        cv2.putText(pose_frame, f'Body angle: {body_straight_form}', [900, 100], #[900, 100] for portrait views, [50, 250] for phones
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 70, 190), 2, cv2.LINE_AA)
        
        #preparing to display
        converted_squat_display = cv2.cvtColor(pose_frame, cv2.COLOR_RGB2BGR)
        display = converted_squat_display

    #a black square with white text indicating where the camera toggle is
    mode_text = exercise_module[mode_selector]
    cv2.rectangle(display, (50, 200), (300, 400), (0, 0, 0), -1)
    cv2.putText(display, mode_text, [75, 250],
                cv2.FONT_HERSHEY_SIMPLEX, 1, (250, 250, 250), 2, cv2.LINE_AA)

    cv2.imshow('Exercise page', display)
    key = cv2.waitKey(1) & 0XFF

    #quits on q
    if key == ord('q'):
        break

    #deploys squat mathematics and pose landmark on s
    if key == ord('s'):
        mode_selector = 2

    #deploys pushup mathematics and pose landmark on p
    if key == ord('p'):
        mode_selector = 1

    #returns to default frames
    if key == ord('d'):
        mode_selector = 0

cap.release()
cv2.destroyAllWindows()
