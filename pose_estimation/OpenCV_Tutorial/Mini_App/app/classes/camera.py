from app.classes.video_source import VideoSource
from app.classes.user import User
import cv2 as cv
from datetime import datetime

"""this class is created as a template that will pass off instances
of a camera feed so that images can be taken and videos recorded.

the camera is passed as an API method fed to the HTML
"""

class Camera(User):
    def __init__(self, source):

        """to initialize the camera, a camera source is given as a constructor argument
        to begin a filming process with the class methods.

        The camera source is obtained dynamically and conditionally, based on the user request.

        Three different sources are accepted:
        1. the relative path to the user's hardware
        2. a camera connected to an IP device.
        3. a prerecorded .mp4 video"""

        self.source = source


    def video_camera(self):
        """helper function to open the camera feed"""
        capture = cv.VideoCapture(self.source)
        return capture


    def capture_frames(self, frame): #removed self for a quick test
        """this function captures the ongoing frames with cv2.read()

        Create a loop that runs while the video_camera() object is opened.
        
        To separate concerns, a different function will be created to
        release the window and close the camera feed."""

        return frame.read()


    def display_window(self, feed):
        """this is a function to display a window.

        The function takes the following argument:
        1. The frames of a cv2.VideoCapture().read() object

        WARNING: must be used with capture.isOpened() through a while loop"""
        return cv.imshow('Live feed', feed)

    def take_picture(self, feed):
        """this function allows the user to take a picture based on the
        current operating camera feed

        The file saved contains the super().first_name from the User class
        and the current time it was taken at."""
        name = super().first_name
        return cv.imwrite(f'{name}_{datetime.now()}.jpg', feed)


    def record_video_start():
        """this function allows the user to record a video.

        the video's name is written as a formatted string of the super().first_name
        of the inherited user class and the current time it is recorded at.

        The function is fetched to start the recording, but not stop it."""
        pass


    def record_video_end():
        """this function stops recording of a video.

        the closing argument of the function is the writing of the video into
        the database or the current directory, with the name of the user and the
        current time it was filmed at."""
        pass

    def exit_key(self, delay=1):
        """Helper function to prepare the exit key.

        Activated with an event listener on front end JavaScript."""
        return cv.waitKey(delay)


    def release_window(self, capture):
        """this is a helper function to release the camera window and destroy all
        opened windows, ensuring a success return status of the camera object and closing
        of the camera feed process."""
        capture.release()
        cv.destroyAllWindows()


    def to_dict(self):
        """this is a test method that takes the camera object and sends its components
        to the facade"""
        return {
            'camera': self.video_camera(),
            'frames': self.capture_frames(),
            'display': self.display_window(),
            'take_pic': self.take_picture(),
            'start_rec': self.record_video_start(),
            'stop_rec': self.record_video_end(),
            'rel_window': self.release_window()
        }
