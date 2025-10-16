"""this function is a test created by chatgpt to tutor me in pose estimation, opencv,
data compiling and camera functionality. if all goes accordingly, we should be able
to start a process to open a camera, record movement and close it. This is the first of 
many tests."""

print('Checkpoint #1: Initializing packages.')
import numpy as np
#checkpoint to successfully import opencv
import cv2
print('Checkpoint #2: imported OpenCV successfully.')
print(cv2.__version__)
print()

#checkpoint to successfully import mediapipe
import mediapipe as mp
print('Checkpoint #3: imported mediapipe successfully')
print(mp.__version__)
print()

#checkpoint to successfully import tensorflow
#import torch
#import torchvision
#print('Checkpoint #4: imported torch and torchvision successfully.')
#print(torch.__version__)
#print(torchvision.__version__)
#print()

# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
print('Checkpoint #3: initializing the pose estimation landmark')
#object for drawing utilities(our pose landmark will be drawn by using this)
mp_drawing = mp.solutions.drawing_utils
print('Checkpoint #4: importing the drawing utilities from MediaPipe.')
# Start webcam
#Camera taken from iPhone sharing the same WiFi port as laptop
cap = cv2.VideoCapture('http://192.168.0.16:4747/video')

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
        right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
        left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
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
    keypoints, descritors = cv2.ORB_create().detectAndCompute(fixed_frames, None)
    keyframes = cv2.drawKeypoints(fixed_frames, keypoints,  None, color=(255, 0, 255), flags=0)

    #adding conditional clause to determine our mode and update our frames
    if mode_selector == 1:
        result = fixed_frames

    elif mode_selector == 2:
        result = custom_mediapipe_conversion

        #putting text over right shoulder
        cv2.putText(result,
                    'Right Shoulder',#str(right_shoulder), 
                    tuple(np.multiply(right_shoulder, [380, 1260]).astype(int)), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (112, 0, 255), 2)

        #putting test over left shoulder
        cv2.putText(
            result,
            'Left Shoulder',
            tuple(np.multiply(left_shoulder, [760, 1260]).astype(int)), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (112, 0, 255), 2)

    elif mode_selector == 3:
        result = keyframes
    
    elif mode_selector == 4:
        result = default_mediapipe_conversion
    

    mode_text = camera_mode[mode_selector]

    #putting test over my window
    cv2.putText(result, mode_text, (360, 30), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
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
