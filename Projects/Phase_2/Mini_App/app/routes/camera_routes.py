"""writing all CRUD operations for the application"""

from flask import Flask, Blueprint, render_template, Response, send_file, jsonify
from app.classes.threaded_cam import CameraThreaded
import io


camera_blueprint = Blueprint('camera', __name__)
camera = CameraThreaded('http://192.168.0.3:4747/video')

@camera_blueprint.route('/')
def index():
    return render_template('index.html')

@camera_blueprint.route('/vid')
def video_feed():
    def generate():
        while True:
            frame_bytes = camera.get_encoded_frame()
            if frame_bytes:
                 yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@camera_blueprint.route('/snapshot')
def take_snapshot():
    frame_bytes = camera.get_encoded_frame()
    return send_file(io.BytesIO(frame_bytes), mimetype='image/jpeg', download_name='snapshot.jpg')

@camera_blueprint.route('/fps')
def fps():
    return jsonify({'fps': camera.get_fps()})
