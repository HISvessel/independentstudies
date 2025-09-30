"""writing all CRUD operations for the application"""

from flask import Flask, Blueprint, render_template, Response, send_file, jsonify
from app.classes.threaded_cam import CameraThreaded
import io
import logging


camera_blueprint = Blueprint('camera', __name__)
camera = CameraThreaded('http://192.168.9.175:4747/video').start()
logger = logging.getLogger(__name__)


@camera_blueprint.route('/')
def index():
    logger.info('Serving webpage')
    return render_template('index.html')

@camera_blueprint.route('/video_feed')
def video_feed():
    logger.info('Client requesting camera service')
    try:
        def generate():
            while True:
                frame_bytes = camera.get_encoded_frame()
                if frame_bytes:
                    yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')
    except Exception as e:
        logger.error(f'Service could not be provided: {e}', exc_info=True)
        return {"Error": str(e)}, 500


@camera_blueprint.route('/snapshot')
def take_snapshot():
    logger.info("Snapshot requested")
    frame_bytes = camera.get_encoded_frame()
    return send_file(io.BytesIO(frame_bytes), mimetype='image/jpeg', download_name='snapshot.jpg')

@camera_blueprint.route('/fps')
def fps():
    return jsonify({'fps': camera.get_fps()})
