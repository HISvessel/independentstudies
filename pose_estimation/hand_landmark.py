"""this function opens a camera and places landmarks for hand
movement trackning using mediapipe"""

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2
import numpy as np
from google.collab.patches import cv2_imshow

MARGIN = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54) # vibrant green

def draw_landmarks_on_image(rgb_image, detection_result):
  hand_landmarks_list = detection_result.hand_landmarks
  handedness_list = detection_result.handedness
  annotated_image = np.copy(rgb_image)

  # Loop through the detected hands to visualize.
  for idx in range(len(hand_landmarks_list)):
    hand_landmarks = hand_landmarks_list[idx]
    handedness = handedness_list[idx]

    # Draw the hand landmarks.
    hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    hand_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
    ])
    mp.solutions.drawing_utils.draw_landmarks(
      annotated_image,
      hand_landmarks_proto,
      mp.solutions.hands.HAND_CONNECTIONS,
      mp.solutions.drawing_styles.get_default_hand_landmarks_style(),
      mp.solutions.drawing_styles.get_default_hand_connections_style())

    # Get the top left corner of the detected hand's bounding box.
    height, width, _ = annotated_image.shape
    x_coordinates = [landmark.x for landmark in hand_landmarks]
    y_coordinates = [landmark.y for landmark in hand_landmarks]
    text_x = int(min(x_coordinates) * width)
    text_y = int(min(y_coordinates) * height) - MARGIN

    # Draw handedness (left or right hand) on the image.
    cv2.putText(annotated_image, f"{handedness[0].category_name}",
                (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX,
                FONT_SIZE, HANDEDNESS_TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA)

  return annotated_image



base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
#HandLandMarker = mp.tasks.vision.HandLandmarker
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)

detector = vision.HandLandmarker.create_from_options(options)
#this creates a hand landmarker instance with the video mode
#options = HandLandMarkerOptions(base_options=base_options(model_asset_path='path/to/model.task'), running_mode=VisionRunningMode.VIDEO)

image = mp.Image.create_from_file("./lena.jpg")

detection_result = detector.detect(image)

annotated_image = draw_landmarks_on_image()
cv2.imshow(cv2.cvtCOLOR(annotated_image, cv2.COLOR_RGB2BGR))