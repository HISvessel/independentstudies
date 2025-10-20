"""this function is a test created by chatgpt to tutor me in pose estimation, opencv,
data compiling and camera functionality. if all goes accordingly, we should be able
to start a process to open a camera, record movement and close it. This is the first of 
many tests."""

import numpy as np
import cv2
import mediapipe as mp
from form_analysis import FormAnalyzer


# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Start webcam
#Camera taken from iPhone sharing the same WiFi port as laptop
cap = cv2.VideoCapture('http://192.168.0.8:4747/video')

#global result printing frame object
result = None

#data structure object that updates the frames by selecting the mode
#modes are selected at the press of a key
mode_selector = 1 #default mode
camera_mode = {
    1: 'preview', 
    2: 'custom pose',
    3: 'ORBs',
    4: 'default pose'
}

if not cap.isOpened():
    print('Cannot open camera. It has not been accessed.')

#human detection module:
#hog = cv2.HOGDescriptor()
#hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    ret, frame = cap.read()
    if not ret:
        break

    #rotating imaage clockwise
    fixed_frames = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)


    # Convert frame to RGB (MediaPipe requires RGB input)
    # Creating buffers for two separate mediapipe frames
    rgb_frame_1 = cv2.cvtColor(fixed_frames, cv2.COLOR_BGR2RGB)
    rgb_frame_2 = cv2.cvtColor(fixed_frames, cv2.COLOR_BGR2RGB)

    pose_p1 = pose.process(rgb_frame_1)
    pose_p2 = pose.process(rgb_frame_2)


    if pose_p1.pose_landmarks:
        #preparing retrieving landmarks individually for our left and right shoulder
        landmarks = pose_p1.pose_landmarks.landmark
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

        right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
        left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        #print(f'Left shoulder is {l_shoulder}')
        #print(f'Right shoulder is {r_shoulder}')
        #print(f'')
        #print(type(landmarks))
        #print(type(right_shoulder))
        #print(right_shoulder)
        #print(pose_p.pose_landmarks)

        #creating a custom set of connections for the body, this draws connections to everything except the face
        body_connections = frozenset([(0, 11), (0, 12), (0, 23), (0, 24),
                                      (11, 12), (11, 13), (13, 15), (12, 14), (14, 16),
                                      (11, 23), (12, 24), (11, 24), (12, 23), (23, 24),
                                      (23, 25), (24, 26), (25, 27), (26, 28)])
        mp_drawing.draw_landmarks(
            image=rgb_frame_1, #the frames captured by the camera and CV2
            landmark_list=pose_p1.pose_landmarks, #the pose landmarks(points on the limbs)
            connections=body_connections, #the list of connections(lines connecting points)
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(200, 169, 0), thickness=2, circle_radius=3),#specifications for drawing the dots of desired color
            connection_drawing_spec=mp_drawing.DrawingSpec(color=(169, 169, 169), thickness=2)#specifications for drawing the connections to desired color
            )

    if pose_p2.pose_landmarks:
        mp_drawing.draw_landmarks(
            image=rgb_frame_2,
            landmark_list=pose_p2.pose_landmarks,
            connections=mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(200, 169, 0), thickness=2, circle_radius=3),
            connection_drawing_spec=mp_drawing.DrawingSpec(color=(112, 112, 112), thickness=2)
        )
    #converts frames into BGR format for OpenCV
    #stores data frames in a temporal buffer to be exchanged at imshow
    custom_mediapipe_conversion = cv2.cvtColor(rgb_frame_1, cv2.COLOR_RGB2BGR)
    default_mediapipe_conversion = cv2.cvtColor(rgb_frame_2, cv2.COLOR_RGB2BGR)

    #draws keypoints for orbs and places them in edges
    #keyframes are stored in a loaded buffer to place in imshow()
    #keypoints, descritors = cv2.ORB_create().detectAndCompute(fixed_frames, None)
    #keyframes = cv2.drawKeypoints(fixed_frames, keypoints,  None, color=(255, 0, 255), flags=0)

    #adding conditional clause to determine our mode and update our frames
    if mode_selector == 1:
        result = frame

        vertical, horizontal, _ = result.shape

        center_x = horizontal // 2
        center_y = vertical // 2

        #finding the frames of our reticle dimension
        left_superior = (center_x - 360, center_y - 240)
        right_superior = (center_x + 360, center_y - 240)
        left_inferior = (center_x - 360, center_y + 240)
        right_inferior = (center_x + 360, center_y + 240)


        """drawing a red reticle in the center of the camera shot"""
        #horizontal line of the frame reticle
        cv2.line(result, (center_x + 15, center_y), (center_x - 15, center_y), (0, 0, 150), 2)
        
        #the vertical line of the frame reticle
        cv2.line(result, (center_x, center_y + 15), (center_x, center_y - 15), (0, 0, 150), 2)

        #drawing a rectangle to process frames around it
#        reticle = cv2.rectangle(result, (center_x + 360, center_y - 540), (center_x - 360, center_y + 540), (0, 0, 150), 2)

        #(rects, weights) = hog.detectMultiScale(result, winStride=(8, 8), padding=(16, 16), scale=1.05)
        #cv2.putText(result, 'Nobody is inside the square', (720, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 250, 0), 2)
        
        #people_in_frame = 0
        
        #putting text on the corners I wish to iterate through and process information
        cv2.putText(result, f'{left_superior}', left_superior, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 150), 2)
        cv2.putText(result, f'{left_inferior}', left_inferior, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 150), 2)
        cv2.putText(result, f'{right_superior}', right_superior, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 150), 2)
        cv2.putText(result, f'{right_inferior}', right_inferior, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 150), 2)


        #for (x, y, w, h) in rects:
        #    cv2.rectangle(result, (x, y), (x+w, y+h), (0, 255, 0), 1)
        #    people_in_frame += 1
        #    cv2.putText(result, f'People on the square: {people_in_frame}', (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 250, 0), 2)


    elif mode_selector == 2:
        result = custom_mediapipe_conversion
        #form = FormAnalyzer.angle_between(l_shoulder, l_elbow, l_wrist)
        form = FormAnalyzer.calculate_angle([l_shoulder.x, l_shoulder.y], [l_elbow.x, l_elbow.y], [l_wrist.x, l_wrist.y])
        #putting text over right shoulder
        cv2.putText(result,
                    'Right Shoulder',#str(right_shoulder), 
                    tuple(np.multiply(right_shoulder, [380, 1260]).astype(int)), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (112, 0, 255), 2)

        #putting test over left shoulder
        cv2.putText(result,
                    'Left Shoulder',
                    tuple(np.multiply(left_shoulder, [760, 1260]).astype(int)), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (112, 0, 255), 2)
        
        cv2.putText(result, 
                    f'{form}',
                    [30, 30],
                    #tuple(np.multiply([l_wrist.x, l_wrist.y], [760, 1800]).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        if form > 90:
            cv2.putText(result,
                        'You bent to 90 degrees',
                        [120, 900],
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2)


    elif mode_selector == 3:
        #result = keyframes
        vertical, horizontal, _ = result.shape
        center_x = horizontal // 2
        center_y = vertical // 2
        reticle = cv2.rectangle(result, (center_x + 360, center_y - 360), (center_x - 360, center_y + 360), (0, 0, 150), 2)

        #for pixels_x in range(280, 1000):
        #    for pixels_y in range(120, 600):
        keypoints, descritors = cv2.ORB_create().detectAndCompute(result[280:1000, 120:600], None)
        keyframes = cv2.drawKeypoints(result, keypoints,  None, color=(255, 0, 255), flags=0)
                #continue
        result = keyframes
    
    elif mode_selector == 4:
        result = default_mediapipe_conversion
    

    mode_text = camera_mode[mode_selector]

    #putting test over my window
    #cv2.putText(result, mode_text, (360, 30), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
    cv2.imshow("Pose Estimation", result)
    key = cv2.waitKey(1) & 0XFF

    #draws customized body landmarks at the press of the c keyboard
    if key == ord('c'):
        print('Selecting the frames with custom made pose estimation drawing.')
        mode_selector = 2

    #draws ORBs upon detected image edges at the press of the o keyboard
    elif key == ord('o'):
        print('Selecting the frames to add orbs on image edges.')
        mode_selector = 3

    #presets the default frames with no effects at the press of the d keyboard
    elif key == ord('d'):
        print('Selecting the default frames.')
        mode_selector = 1

    #draws the default pose estimation landmark at the press of the p keyboard
    elif key == ord('p'):
        print('Selecting the frames with the default pose estimation drawing.')
        mode_selector = 4

    # Exit on pressing q on the keyboard
    elif key == ord('q'):
        print('Exiting. Goodbye...')
        break



# Release resources
cap.release()
cv2.destroyAllWindows()
