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
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

        self.thread = threading.Thread(target=self.update, daemon=True)
        self.thread.start()

        #fps tracking
        self._fps = 0.0
        self._frame_count = 0
        self._last_time = time.time()


    def update(self):
        while self.running:
            #time.sleep(0.5)
            success, frame = self.capture.read()
            if success and frame is not None:
                self.frame = frame
                #print(f'[DEBUG] Got frame of shape {frame.shape}')
                #self._frame_count += 1

                #now = time.time()
                #if now - self._last_time >= 1.0:
                #    self._fps = self._frame_count / (now - self._last_time)
                #    self._frame_count = 0
                #    self._last_time = now
            else:
                print('Frame read failed. Failed at class level.')
                break
            #time.sleep(0.3)

    def get_frame(self):
        """Return latest frame as numpy array"""
        return self.frame

    def get_encoded_frame(self):
        """Return frame as JPEG bytes for API use"""
        if self.frame is None:
            print('No frame available yet...')
            #return None
            time.sleep(0.3)
        print('Stage 2: looking to go beyond the previous frame available message')
        success, buffer = cv.imencode('.jpg', self.frame)
        if not success:
            print('Could not encode frames. Failed at class level.')
            return None
        print('Captured frames, now returning.')
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
