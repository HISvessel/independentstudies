import cv2 as cv
from app.classes.user import User
from datetime import datetime
import threading
import time
import asyncio
from datetime import datetime



class CameraThreaded(User):
    def __init__(self, source):#, warmup_frames=5):
        self.source = source
        self.capture = cv.VideoCapture(self.source)
        self.frame = None
        self.running = True
        self.ready = threading.Event()
        self.lock = threading.Lock()

        #creating a camera warmup counter
        #self.warmup_frames = warmup_frames
        #self._warmup_count = 0

        self.thread = threading.Thread(target=self.update, daemon=True)
        self.thread.start()


        #fps tracking
        #self._fps = 0.0
        #self._frame_count = 0
        #self._last_time = time.time()


    def update(self):
        while self.running:
            success, frame = self.capture.read()
            if success and frame is None:
                print(f'[CLASS] Updating frame value failed at {datetime.now()}.')
                #time.sleep(0.3)
            
            """contain within the same scope for if clauses"""
            #if success and frame is not None:
            with self.lock:
                self.frame = frame
            #self._frame_count += 1

            #if not self.ready.is_set():
            #        #this starts the threading Event().set() at the time when the count is larger than the preset frames
            #        self._warmup_count += 1
            #        if self._warmup_count >= self.warmup_frames:
            #            self.ready.set()
            """end of container"""

                #now = time.time()
                #if now - self._last_time >= 1.0:
                #    self._fps = self._frame_count / (now - self._last_time)
                #    self._frame_count = 0
                #    self._last_time = now
            #else:
            #    print('Frame read failed. Failed at class level.')
            #    time.sleep(0.1)

    def wait_until_ready(self, timeout=5.0):
        """blocks thread until function is ready"""
        ready = self.ready.wait(timeout)
        if not ready:
            print(f'[CLASS] Waiting for camera to be ready. Timestamped at {datetime.now()}')
        return ready
    

    def get_frame(self):
        """Return latest frame as numpy array"""
        return self.frame

    #async 
    def get_encoded_frame(self):
        """Return frame as JPEG bytes for API use"""
        if self.frame is None:
            print(f'[CLASS] Frames are currently none, they have not been read for encoding. Triggered at {datetime.now()}')
            return None

        #success, buffer = cv.imencode('.jpg', self.frame, [cv.IMWRITE_JPEG_QUALITY, 85])
        #print(f'[CLASS] Encoding at {datetime.now()}')
        success, buffer = cv.imencode('.jpg', self.frame, [cv.IMWRITE_JPEG_QUALITY, 85])
        if not success:
            print(f'[CLASS] Could not encode frames. Timestamped at {datetime.now()}')
            return None
        #print(type(buffer))
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
