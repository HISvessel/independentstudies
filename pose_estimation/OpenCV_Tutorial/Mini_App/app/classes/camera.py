from app.classes.video_source import VideoSource
from app.classes.user import User
import cv2 as cv
from datetime import datetime

"""this class is created as a template that will pass off instances
of a camera feed so that images can be taken and videos recorded.

the camera is passed as an API method fed to the HTML
"""

class Camera(User):
    def __init__(self):
        source = [0, 1, 2, 'http://192.168.0.3:4747/video']
        picture_button = cv.imwrite(f'{super().first_name}_{super().last_name}_{datetime.now()}.jpg')
        record_button = cv.VideoWrite(f'{super().first_name}_{super().last_name}_{datetime.now()}.mp4')


    def video_camera(self):
        """helper function to open the camera feed"""
        capture = cv.VideoCapture('http://192.168.0.3:4747/video')
        return capture


    def show_screen(self):
        """this function displays the recording screen on the website
        
        When called by the front end, it should run asynchronously.
        
        To separate concerns, a different function will be created to
        release the window and close the camera feed"""

        camera = self.video_camera()
        while camera.isOpened():
            success, camera_feed = camera.read()
            if not success:
                print('Unable to display camera screen')
                break
            return cv.imshow('Online camera', camera_feed)


    def take_picture(self, image):
        """this function should allow the user to take a picture based on the
        current operating camera feed"""
        name = super().first_name
        return cv.imwrite(f'{name}_{datetime.now()}.jpg', image)


    def record_video_start():
        """this function allows the user to record a video"""
        pass


    def record_video_end():
        """this function stops recording of a video"""
        pass


    def release_window(self):
        """this is a helper function to release the camera window"""
        try:
            camera = self.video_camera()
            camera.release()
        except:
            if camera.isOpened() == False:
                print('Cannot close camera, it was never opened')


    def send_to_database():
        """this function sends the photo or video taken to the database"""
        pass