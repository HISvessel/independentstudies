"""this script runs the application"""
from flask import Flask
from flask_socketio import SocketIO
from app.classes.threaded_cam import CameraThreaded
from app.routes.camera_woth_socket import video_feed
#import eventlet


def create_app():
    #from app.routes.camera_routes import camera_blueprint
    from app.routes.camera_woth_socket import live_feed_bp

    app = Flask(__name__, template_folder='fhtml')
    app.config['SECRET_KEY'] = 'secret!'
    socketio = SocketIO()
    socketio.init_app(app) #prepare to erase this if necessary
    #app.register_blueprint(camera_blueprint)
    app.register_blueprint(live_feed_bp)
    # video_feed(socketio)
    #eventlet.sleep(0.1) #testing concurrency here.

    #the issue lies here: the camera is starting from here
    #and not from the video feed function.
    #cam = CameraThreaded(source='http://192.168.0.9:4747/video')
    #init_camera_feed(cam, socketio)

    return app, socketio
