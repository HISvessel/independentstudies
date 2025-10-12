"""this function is a test created by chatgpt to tutor me in pose estimation, opencv,
data compiling and camera functionality. if all goes accordingly, we should be able
to start a process to open a camera, record movement and close it. This is the first of 
many tests."""

print('Checkpoint #1: Initializing packages.')

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
#import tensorflow as tf
#print('Checkpoint #4: imported tensorflow successfully.')
#print(tf.__version__)
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
    2: 'pose',
    3: 'orbs'
}

if not cap.isOpened():
    print('Cannot open camera. It has not been accessed.')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    
    # Convert frame to RGB (MediaPipe requires RGB input)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pose_p = pose.process(rgb_frame)
    if pose_p.pose_landmarks:
        mp_drawing.draw_landmarks(
            rgb_frame, #the frames captured by the camera and CV2
            pose_p.pose_landmarks, #the pose landmarks
            mp_pose.POSE_CONNECTIONS #the list of connections
            )
    #converts frames into BGR format for OpenCV
    #stores data frames in a temporal buffer to be exchanged at imshow
    mediapipe_conversion = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)

    #draws keypoints for orbs and places them in edges
    #keyframes are stored in a loaded buffer to place in imshow()
    keypoints, descritors = cv2.ORB_create().detectAndCompute(frame, None)
    keyframes = cv2.drawKeypoints(frame, keypoints,  None, color=(255, 0, 0), flags=0)

    #adding conditional clause to determine our mode and update our frames
    if mode_selector == 1:
        result = frame
    elif mode_selector == 2:
        result = mediapipe_conversion
    elif mode_selector == 3:
        result = keyframes
    

    mode_text = camera_mode[mode_selector]

    #putting test over my window
    cv2.putText(result, mode_text, (450, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Pose Estimation", result)
    key = cv2.waitKey(1) & 0XFF

    #draws body landmarks at the press of the p keyboard
    if key == ord('p'):
        print('Selecting the frames to deploy pose landmarks on the screen')
        print(f'The converted mediapipe frames id is {id(mediapipe_conversion)}')
        mode_selector = 2
        print(id(result))
    
    elif key == ord('o'):
        #keypoints, descritors = cv2.ORB_create().detectAndCompute(frame, None)
        #keyframes = cv2.drawKeypoints(frame, keypoints,  None, color=(255, 0, 0), flags=0)
        print('Selecting the frames to add orbs on image edges')
        print(f'The keyframe id is {id(keyframes)}')
        mode_selector = 3


    elif key == ord('d'):
        print('Selecting the default frames.')
        print(f'The frames id is {id(frame)}')
        mode_selector = 1

    # Exit on pressing 'q'
    elif key == ord('q'):
        print('Exiting. Goodbye...')
        break



# Release resources
cap.release()
cv2.destroyAllWindows()
