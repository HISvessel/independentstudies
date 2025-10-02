import base64
from flask import render_template, Blueprint
from flask_socketio import SocketIO
from app.classes.threaded_cam import CameraThreaded
from threading import Lock
import eventlet
import time



"""this module is a different approach at uploading encoded frames into
a miniature web application using websockets"""

live_feed_bp = Blueprint('live_feed', __name__)
#camera = None
thread = None
thread_lock = Lock()
#socketio = SocketIO()

@live_feed_bp.route('/')
def index():
    return render_template('index.html')


def video_feed(socketio):
    #takes frames as encoded inputs
    
    camera = CameraThreaded(source='http://192.168.0.9:4747/video')
    #print(f'Running the is Opened clause. Outcome: {camera.capture.isOpened()}.')
    while True:
        #print(f'[DEBUG] Testing input time for thread')
        if camera.capture.isOpened() == False:
            print('Error reading from source.')
            return None
        #delays the callstack to prepare the frames at class 
        frames = camera.get_encoded_frame()
        if frames is None:
            print("Failure capturing frames for encoding. Failed at video feed.")
            break
        print(frames)
        time.sleep(0.2)
        JPGs = base64.b64encode(frames).decode('utf-8')
        #print(JPGs)
        socketio.emit('frame', JPGs)
        #print(f'[DEBUG] Will the thread reach this point?')


@live_feed_bp.route('/stop_feed')
def exit_feed():
    pass