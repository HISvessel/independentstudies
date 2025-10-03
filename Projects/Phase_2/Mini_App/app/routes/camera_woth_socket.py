import base64
from flask import render_template, Blueprint
from app.classes.threaded_cam import CameraThreaded
import time
import asyncio
from datetime import datetime
import cv2


"""this module is a different approach at uploading encoded frames into
a miniature web application using websockets"""


live_feed_bp = Blueprint('live_feed', __name__)
#camera = None
#feed_task_running = False

#camera = CameraThreaded(source='http://192.168.9.175:4747/video')

@live_feed_bp.route('/')
def index():
    return render_template('index.html')

@live_feed_bp.route('/ping')
def pong():
    return 'pong'

async def encode_frames(cam):
    await asyncio.sleep(0.3)
    success, buffer = cv2.imencode('.jpg', cam, [cv2.IMWRITE__QUALITY, 85])
    if not success:
        print(f'[FEED] Sleeping asyncio did not work.')
        
    return buffer.tobytes()

async def b_encoder(frames):
    await asyncio.sleep(0.4)
    await frames
    return base64.b64encode(frames).decode('utf-8')

def video_feed(socketio, camera):
    #takes frames as encoded inputs
    #global camera
    #moving the camera init elsewhere
    #camera = CameraThreaded(source='http://192.168.0.9:4747/video')#, warmup_frames=10)


    print(f'[FEED] Camera opened at {datetime.now()}. Outcome: {camera.capture.isOpened()}.')
    socketio.sleep(0.6)
    while True:
        if camera.capture.isOpened() == False:
            print('Error reading from source.')
            continue
        #delays the callstack to prepare the frames at class 
        frames = camera.get_encoded_frame()
        if frames is not None:
            #print(f'[FEED] Frames are encoded at {datetime.now()}')
        #print(frames)
        #if frames is None:
            #watch exactly WHEN error message presents itself
            #print(f"[FEED] Failure capturing frames for encoding. Failed at {datetime.now()}")
            #continue
            JPGs = base64.b64encode(frames).decode('utf-8')
            #print(JPGs)

        socketio.emit('frame', JPGs)
        #time.sleep
        socketio.sleep(0.01)
        #print(f'[DEBUG] Will the thread reach this point?')
    @socketio.on('connect')
    def handle_connect():
        print()
        emit()


""" This is a mess clause made that does not work   
    while True:
        if camera is None:
            print('[FEED] Camera stopped, ending feed taks')
            break

        
        frames = camera.get_encoded_frame()

        if frames is None:
            print("Waiting for frames still")
            time.sleep(0.1)
            continue

        JPGs = base64.b64encode(frames).decode('utf-8')
        socketio.emit('frame', JPGs)
        time.sleep(0.033)

def init_socketio(socketio, source='http://192.168.9.175.4747/video'):
    #registers socketio event handlers for camera feed.
    #Called during app initialization
    global camera, feed_task_running
    @socketio.on('connect')
    def handle_connect():
        global camera, feed_task_running

        if camera is None:
            camera = CameraThreaded(source)
        
        if not feed_task_running:
            feed_task_running = True
            socketio.start_background_task(video_feed, socketio)
"""

@live_feed_bp.route('/stop_feed')
def exit_feed():
    pass