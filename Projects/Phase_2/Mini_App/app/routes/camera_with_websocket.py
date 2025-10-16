import base64
from flask import render_template, Blueprint
from app.classes.threaded_cam import CameraThreaded
import asyncio
from datetime import datetime
from flask_socketio import SocketIO, Namespace, join_room, close_room, leave_room


"""this module is a different approach at uploading encoded frames into
a miniature web application using websockets"""

homepage = Blueprint('homepage', __name__)
live_feed_bp = Blueprint('live_feed', __name__)

#globalized objects for universal function callbacks
camera = None
socket = SocketIO()
socket_room = Namespace()

@socket_room.rooms('id', 'new private room')

@homepage.route('/')
def home():
    return render_template('home.html')

@live_feed_bp.route('/camera')
def index():
    return render_template('index.html')


#testing async method. Project for another day
"""async def encode_frames(cam):
    await asyncio.sleep(0.3)
    success, buffer = cv2.imencode('.jpg', cam, [cv2.IMWRITE__QUALITY, 85])
    if not success:
        print(f'[FEED] Sleeping asyncio did not work.')
        
    return buffer.tobytes()

#testing async method. Project for another day
async def b_encoder(frames):
    await asyncio.sleep(0.4)
    await frames
    return base64.b64encode(frames).decode('utf-8')

def emit_video_feed(camera):
    #camera = CameraThreaded(source='http://192.168.0.16:4747/video')


    print(f'[FEED] Camera opened at {datetime.now()}. Outcome: {camera.capture.isOpened()}.')
    #eventlet.sleep(2.0)
    while True:
        if camera.capture.isOpened() == False:
            print('Error reading from source.')
            continue
        #delays the callstack to prepare the frames at class 
        frames = camera.get_encoded_frame()
        #if frames is not None:
            #print(f'[FEED] Frames are encoded at {datetime.now()}')
        #print(frames)
        if frames is None:
            #watch exactly WHEN error message presents itself
            print(f"[FEED] Failure capturing frames for encoding. Failed at {datetime.now()}")
            continue
        JPGs = base64.b64encode(frames).decode('utf-8')
        #print(JPGs)
        return JPGs
"""

def video_feed(socketio, camera):

    print(f'[FEED] Camera opened at {datetime.now()}. Outcome: {camera.capture.isOpened()}.')
    socketio.sleep(0.6)
    if camera.capture.isOpened() == False:
        exit

    while True:
        if camera.capture.isOpened() == False:
            print('Error reading from source.')
            break
        #delays the callstack to prepare the frames at class 
        frames = camera.get_encoded_frame()
        #if frames is not None:
            #print(f'[FEED] Frames are encoded at {datetime.now()}')
        #print(frames)
        if frames is None:
            #watch exactly WHEN error message presents itself
            print(f"[FEED] Failure capturing frames for encoding. Failed at {datetime.now()}")
            continue
        JPGs = base64.b64encode(frames).decode('utf-8')
        socketio.emit('frame', JPGs, room='private_feed')
        socketio.sleep(0.01)
        #print(JPGs)

def interrupt_feed(socketio):
    socketio.close_room('private_feed')


def stop_feed(socketio, camera):
    try:
        camera.stop()
        socketio.close_room('private_feed')
    except RuntimeError:
        print('Cannot stop camera feed.')

def enter_room(socket):
    @socket.on('connect')
    def connect():
        global camera
        if camera is None:
            camera = CameraThreaded(source="http://192.168.0.16:4747/video")
        if camera.capture.isOpened() == True:
            join_room('private_feed')
            socket.start_background_task(video_feed, socket, camera)
            #socketio.on_event('free')

#def leave_room(socket):
    #registering a websocket free event to manually turn off camera
    @socket.on('free')
    def free():
        global camera
        print('[APP] this event has been reached')
        stop_feed(socket, camera)
        camera = None

    #registering a websocket disconnect for interruptions and unwanted events
    @socket.on('disconnect')
    def disconnect():
        """if client disconnects from the websocket and was previously
        connected, they can enter the room.
        
        The task would be to leave a trace or have a session that leaves
        breadcrumbs which can be stored for a timeout period. And if it is
        the correct person, and they were previously in the room, they can enter back.
        
        
        In the meantime, they are kicked out of the room."""
        global camera
        close_room('private_room')
        #leave_room('private_room')
        stop_feed(socket, camera)
        camera = None