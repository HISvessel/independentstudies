import base64
from flask import render_template, Blueprint
from flask_socketio import SocketIO
from threading import Lock



"""this module is a different approach at uploading encoded frames into
a miniature web application using websockets"""

live_feed_bp = Blueprint('live_feed', __name__)
camera = None
thread = None
thread_lock = Lock()
#socketio = SocketIO()


def init_camera_feed(cam_instance, socketio):
    global camera, thread
    camera = cam_instance

    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=video_feed, socketio=socketio)

def video_feed(socketio):
    #takes frames as encoded inputs
    while camera and camera.running:
        frames = camera.get_encoded_frame()
        if not frames:
            print("Failure encoding frames")
        JPGs = base64.b64encode(frames).decode('utf-8')
        socketio.emit('frame', JPGs)

@live_feed_bp.route('/')
def index():
    return render_template('index.html')

#@live_feed_bp.route('/stop_feed')
#def exit_feed():
#    pass