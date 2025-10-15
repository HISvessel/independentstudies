"""this script runs the application"""
from flask import Flask
from flask_socketio import SocketIO, emit
from app.classes.threaded_cam import CameraThreaded



def create_app():
    from app.routes.camera_with_websocket import live_feed_bp, homepage, stop_feed, video_feed

    app = Flask(__name__, template_folder='fhtml')
    app.config['SECRET_KEY'] = 'secret!'
    socketio = SocketIO()
    socketio.init_app(app)
    app.register_blueprint(live_feed_bp)
    app.register_blueprint(homepage)
    #camera = CameraThreaded(source="http://192.168.0.16:4747/video")

    #registering my own events for socketio
    @socketio.on('connect')
    def connect():
        camera = CameraThreaded(source="http://192.168.0.16:4747/video")
        socketio.start_background_task(video_feed, socketio, camera)
        #emit('frame', emit_video_feed(camera))
        #socketio.sleep(0.01)

    @socketio.on('disconnect')
    def disconnect():
        emit('free', stop_feed(socketio))

    return app, socketio
