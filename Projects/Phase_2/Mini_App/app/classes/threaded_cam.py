import cv2 as cv
from app.classes.user import User
from datetime import datetime
import threading
import time



class CameraThreaded(User):
    def __init__(self, source):
        self.source = source
        self.capture = cv.VideoCapture(self.source)
        self.frame = None
        self.running = True
        self.thread = threading.Thread(target=self.update, daemon=True)
        self.thread.start()

        #fps tracking
        self._fps = 0.0
        self._frame_count = 0
        self._last_time = time.time()


    def update(self):
        while self.running:
            success, frame = self.capture.read()
            if success and frame is not None:
                self.frame = frame
                self._frame_count += 1
            else:
                print('Frame read failed. Failed at class level.')

                #update FPS every second
                now = time.time()
                if now - self._last_time >= 1.0:
                    self._fps = self._frame_count / (now - self._last_time)
                    self._frame_count = 0
                    self._last_time = now

    def get_frame(self):
        """Return latest frame as numpy array"""
        return self.frame

    def get_encoded_frame(self):
        """Return frame as JPEG bytes for API use"""
        if self.frame is None:
            print('No frame available yet...')
            return None
        success, buffer = cv.imencode('.jpg', self.frame)
        if not success:
            print('Could not encode frames. Failed at class level.')
            return None
        return buffer.tobytes()

    def take_picture(self):
        if self.frame is not None:
            name = super().first_name
            return cv.imwrite(f'{name}_{datetime.now()}.jpg', self.frame)

    def get_fps(self):
        return round(self._fps, 2)

    def stop(self):
        self.running = False
        self.thread.join()
        self.capture.release()
        cv.destroyAllWindows()
