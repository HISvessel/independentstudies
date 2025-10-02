"""this is the file in which the app will be run"""
from app import create_app
from app.routes.camera_woth_socket import video_feed
from app.classes.threaded_cam import CameraThreaded

app, socketio = create_app()
#camera

if __name__ == '__main__':
    #try:
    #socketio.start_background_task(video_feed(socketio))
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
    #finally:
    #    camera.stop()