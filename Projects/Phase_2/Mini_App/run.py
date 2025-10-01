"""this is the file in which the app will be run"""
from app import create_app


app, socketio, camera = create_app()


if __name__ == '__main__':
    try:
        socketio.run(app, host='0.0.0.0', port=5000, debug=True)
    finally:
        camera.stop()