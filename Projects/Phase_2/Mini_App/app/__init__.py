"""this script runs the application"""
from flask import Flask
from flask_socketio import SocketIO
from app.classes.threaded_cam import CameraThreaded
from app.routes.camera_woth_socket import init_camera_feed



def create_app():
    #from app.routes.camera_routes import camera_blueprint
    from app.routes.camera_woth_socket import live_feed_bp

    app = Flask(__name__, template_folder='fhtml')
    app.config['SECRET_KEY'] = 'secret!'
    socketio = SocketIO()
    socketio.init_app(app) #prepare to erase this if necessary
    #app.register_blueprint(camera_blueprint)
    app.register_blueprint(live_feed_bp)
    
    cam = CameraThreaded(source='http://192.168.0.9:4747/video')
    init_camera_feed(cam, socketio)

    return app, socketio, cam
