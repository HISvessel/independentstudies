"""this script runs the application"""
from flask import Flask
from app.classes.threaded_cam import CameraThreaded

def create_app():
    app = Flask(__name__, template_folder='fhtml')
    return app
