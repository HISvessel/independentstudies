"""this is the file in which the app will be run"""
from app import create_app
from app.routes.camera_with_websocket import video_feed
import asyncio
from app.classes.threaded_cam import CameraThreaded

app, socketio = create_app()
camera_source = 'http://192.168.9.175:4747/video'

if __name__ == '__main__':
    try:
        camera = CameraThreaded(source='http://192.168.9.175:4747/video')
        socketio.start_background_task(video_feed, socketio, camera)
        socketio.run(app, host='0.0.0.0', port=5000, debug=True, use_reloader=False)
    

    finally:
        camera.stop()
