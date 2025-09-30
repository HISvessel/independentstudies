"""this script runs the application"""
from flask import Flask
from app.classes.threaded_cam import CameraThreaded
from app.routes.camera_routes import camera_blueprint


def create_app():
    app = Flask(__name__, template_folder='fhtml')
    app.register_blueprint(camera_blueprint)

    return app
