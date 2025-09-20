from classes.video_source import VideoSource
import cv2 as cv

"""this class is created as a template that will pass off instances
of a camera feed so that images can be taken and videos recorded.

the camera is passed as an API method fed to the HTML
"""

class Camera(VideoSource):
    def __init__(self):
        self.picture_button = cv.imwrite(f'', self.find_source())
        self.record_button = cv.VideoWrite()

    def image_camera():
        pass

    def video_camera():
        pass

    def take_picture():
        pass

    def record_video():
        pass

    def send_object():
        return None