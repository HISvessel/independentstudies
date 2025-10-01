import base64
from flask import render_template, Blueprint
from flask_socketio import SocketIO
from app.classes.camera import Camera
import cv2 as cv
from app.classes.threaded_cam import CameraThreaded
from threading import Lock
import eventlet



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

#def init_camera_feed(cam_instance, socketio):
#    global camera, thread
#    camera = cam_instance
#
#    with thread_lock:
#        if thread is None:
#           thread = socketio.start_background_task(target=video_feed, socketio=socketio)

#the issue lies here: this function is not being threaded to the socket
def video_feed(socketio):
    #takes frames as encoded inputs
    
    camera = CameraThreaded(source='http://192.168.0.9:4747/video')
    while True: #and camera.running:
        frames = camera.get_encoded_frame()
        if frames is None:
            print("Failure capturing frames for encoding. Failed at video feed.")
            break
        JPGs = base64.b64encode(frames).decode('utf-8')
        socketio.emit('frame', JPGs)
        eventlet.sleep(0.1)

#@live_feed_bp.route('/')
#def index():
#    return render_template('index.html')

#@live_feed_bp.route('/stop_feed')
#def exit_feed():
#    pass