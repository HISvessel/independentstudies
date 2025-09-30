"""this is the file for memory persistence and structure"""


from app.classes.camera import Camera
from app.classes.threaded_cam import CameraThreaded


class Camera_Facade():
    def __init__(self):
        self.camera = Camera()