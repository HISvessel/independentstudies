import base64
from flask import render_template, Blueprint
from flask_socketio import emit
from app.classes.threaded_cam import CameraThreaded



"""this module is a different approach at uploading encoded frames into
a miniature web application using websockets"""

live_feed_bp = Blueprint('live_feed', __name__)
camera = None

cam = CameraThreaded(source='http://192.168.0.9:4747/video')

@live_feed_bp.route('/')
def index():
    return render_template('index.html')

def init_camera_feed(cam_instance):
    global camera
    camera = cam_instance

def video_feed():
    #takes frames as encoded inputs
    if camera:
        frames = cam.get_encoded_frame()
        if not frames:
            print("Failure encoding frames")
        JPGs = base64.b64encode(frames).decode('utf-8')
        emit('frame', JPGs)
        

#@live_feed_bp.route('/stop_feed')
#def exit_feed():
#    pass