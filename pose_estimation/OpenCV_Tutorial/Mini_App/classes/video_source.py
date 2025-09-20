import cv2
from datetime import datetime

"""this is a camera parent class that takes a video source
from the online user and appends it for the camera to function."""

class VideoSource:
    @classmethod
    def find_source(cls):
        video_capture = []
        for source in video_capture:
            if source is True:
                return cls(video_capture.index(source))
            return None