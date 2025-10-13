MediaPipe

Ann open source software cross platform framework created by Google to build pipelines that process perception data(visible, sensorial and audible data) in real time. Pipelines sit between data input and machine output, and it sends processed data from one pipeline to the next(think command line pipelines '|||' ).

This document will be my individual attempt at recording data from the documentation source. it is meant to be used as a guide for myself and for others to utilize, and it will contain the results of all studied functions for the MediaPipe solutions pose estimation and holistic pipelines, since they are the ones that currently interest me the most for a personal project and for a case study on machine learning, data pipelines, computer algorithms, computer behavior, memory access and function callstacks. 

Base requirements: Media Pipelines for pose estimation and holistic solutions require data input from a video feed and an open source framework for recieving and processing image data in a computer friendly way. As such, we will be using Google's OpenCV and a built in camera in two ways: feeding directly from a computer, and an IP camera assisted by the DroidCam application(see the OpenCV path of this repository for further details.)

Commonly used tools:
1. <ins>mediapipe.solutions.pose</ins>
---------------------------------------------------------------------------------------
> pose_pl = mediapipe.solutions.pose 
# we use something like this to load the module pipeline into an object

> Pose = pose_pl.Pose()
# the following object loads the core class from the pose solutions module. The Pose class takes the following arguments:
    1) static_image_mode: boolean -> determines static or dynamic body tracking by the pose estimation landmark, depending on the image recieved. If parameter is set to false, image will read continuously(good for videos). If parameter is true, there will be no tracking enabled.

    2) model_complexity: integer -> value given for the tracking accuracy, where the higher the value, the more accurate it is at the expense of having the model be slower(presumably will make the landmark have latency and thus slow down the feed.) Value ranges between 0 and 2
    
    3) smooth_landmarks: boolean -> if enabled to true, it will apply temporal smoothing, which makes the model behave fluidly instead of jittery.

    4) enable_segmentation: boolean -> enables body segmentation mask(I beleve it is set to false as default).
    
    5) smooth_segmetations: boolean -> smooths segmentation output across multiple frames for stability

    6) min_detection_confidence: float -> 
    7) min_tracking_confidence: float ->
    
The following known methods exist off of the created Pose object:
> Pose.process(image) -> pose model builtin function that reads that takes a single argument, which is the frames it is trying to read.
> Pose.process(image).pose_landmarks -> a tuple like object(presumably) of the captured landmarks. This itself becomes a parameter for the drawing utils solutions that takes a video feed and draws the landmarks that were detected by the pose estimation solution(Read more below). 

> Pose.process().pose_landmarks.landmarks -> By taking the previous object, and adding the landmarks attribute, you can see the values contained by every landmark pinned to the body when the mediapipe solutions processes the images and finds the landmarks. Doing this returns an iterable list of every single landmark with its x y and z axis values behind more pinnable attributes, meaning that in order to select the x y and z axis of whichever landmark, you call: 1) landmark.x for the x axis, 2) landmark.y for the y axis of the selected landmark, 3) landmark.z for the z axis of the selected landmark, and 4) landmark.visibility, a float numerical value indicating how much visibility does the camera have of the selected landmark at the time of recording. The pose_landmarks contain a total of 33 landmarks situated around the body as follows:
    0 - nose
    1 - left eye (inner)
    2 - left eye
    3 - left eye (outer)
    4 - right eye (inner)
    5 - right eye
    6 - right eye (outer)
    7 - left ear
    8 - right ear
    9 - mouth (left)
    10 - mouth (right)
    11 - left shoulder
    12 - right shoulder
    13 - left elbow
    14 - right elbow
    15 - left wrist
    16 - right wrist
    17 - left pinky
    18 - right pinky
    19 - left index
    20 - right index
    21 - left thumb
    22 - right thumb
    23 - left hip
    24 - right hip
    25 - left knee
    26 - right knee
    27 - left ankle
    28 - right ankle
    29 - left heel
    30 - right heel
    31 - left foot index
    32 - right foot index

> Pose.process().pose_landmarks.landmark[i] -> a list of tuple-like object(presumably) that contains information of each of the 33 pose estimation landmarks. 
# Each individual landmark contais the following:
    x and y coordinates = normalized coordinates of float 16 bit integers in between 0 and 1
    z coordinate = a depth coordinate that says how close or how far the landmark is from the camera. 
    visibility = a probability value that the landmark is visible(take occlusions and filtering into accounts for this.)

> Pose.process().pose_world_landmarks -> these are the 3d implementation coordinates of each landmark. 
> Pose.process().segmentation_mask


2. <ins>mediapipe.solutions.hands</ins>
---------------------------------------------------------------------------------------


3. <ins>mediapipe.solutions.holistic</ins>
---------------------------------------------------------------------------------------


4. <ins>mediapipe.solutions.face_mesh</ins>
---------------------------------------------------------------------------------------


5. <ins>mediapipe.solutions.drawing_utils</ins>
---------------------------------------------------------------------------------------
> this complements the previous mediapipe solutions by drawing the models that were created based off of the read frames.
# drawing_utils() takes the following arguments:
    1) image: np.ndarray -> the iage frames that are being read
    2) landmark_list: pose.pose_landmarks -> every landmark targeted presented at runtime
    3) connections: pose.LANDMARK_CONNECTIONS -> draws lines to connect the landmarks as they are programmed by the builtin to connect(eg. connects left arm to left shoulder, right arm to right shoulder, etc.)
    4) landmark_drawing_spec: DrawingSpec ->
    5) connection_drawing_spec: DrawingSpec -> this controls the colors and the thickness for the connections. 
    
> drawing_utils.draw_landmarks() -> 


6. <ins>mediapipe.solutions.drawing_styles</ins>
---------------------------------------------------------------------------------------

