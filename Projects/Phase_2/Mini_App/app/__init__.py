"""this script runs the application"""
from flask import Flask
from flask_socketio import SocketIO, disconnect, join_room, leave_room
from app.classes.threaded_cam import CameraThreaded

camera = None
def create_app():
    from app.routes.camera_with_websocket import live_feed_bp, homepage, video_feed, stop_feed, interrupt_feed

    app = Flask(__name__, template_folder='fhtml')
    app.config['SECRET_KEY'] = 'secret!'
    socketio = SocketIO()
    socketio.init_app(app)
    app.register_blueprint(live_feed_bp)
    app.register_blueprint(homepage)

    #registering websocket connect
    @socketio.on('connect')
    def connect():
        global camera
        if camera is None:
            camera = CameraThreaded(source="http://192.168.0.16:4747/video")
        if camera.capture.isOpened() == True:
            join_room('private_feed')
            socketio.start_background_task(video_feed, socketio, camera)
        #socketio.on_event('free')

    #registering a websocket free event to manually turn off camera
    @socketio.on('free')
    def free():
        global camera
        print('[APP] this event has been reached')
        stop_feed(socketio, camera)
        camera = None

    #registering a websocket disconnect for interruptions and unwanted events
    @socketio.on('disconnect')
    def disconnect():
        """if client disconnects from the websocket and was previously
        connected, they can enter the room.
        
        The task would be to leave a trace or have a session that leaves
        breadcrumbs which can be stored for a timeout period. And if it is
        the correct person, and they were previously in the room, they can enter back.
        
        
        In the meantime, they are kicked out of the room."""
        global camera
        leave_room('private_room')
        stop_feed(socketio, camera)
        camera = None

    return app, socketio
