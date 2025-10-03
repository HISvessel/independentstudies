"""this script runs the application"""
from flask import Flask
from flask_socketio import SocketIO



def create_app():
    from app.routes.camera_woth_socket import live_feed_bp

    app = Flask(__name__, template_folder='fhtml')
    app.config['SECRET_KEY'] = 'secret!'
    socketio = SocketIO()
    socketio.init_app(app)
    app.register_blueprint(live_feed_bp)


    return app, socketio
