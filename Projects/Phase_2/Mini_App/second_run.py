import cv2 as cv
# import eventlet
import time
import base64
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def capture_image():
    cap = cv.VideoCapture('http://192.168.0.9:4747/video')
    while True:
        success, frame = cap.read()

        #handling edge cases for inoperative camera
        if not success:
            print('Cnnot capture frames')
            break

        _, encode = cv.imencode('.jpg', frame)

        #handling error for empty frames
        if frame is None:
            print('Could not encode frames.')
            break

        #prepares encoding and decoding for the HTML
        JPGs = base64.b64encode(encode).decode('utf-8')

        #emits frames when socket is requested
        socketio.emit('frames', JPGs)

        #sleeping to allow for other tasks
        time.sleep(0.01)
    #releases capture once process is done
    cap.release()

if __name__ == '__main__':
    socketio.start_background_task(capture_image)
    socketio.run(app, host='0.0.0.0', port= 5000)
