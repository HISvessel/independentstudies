"""this script runs the application"""
from flask import Flask
#from app.routes.camera_routes import camera_blueprint
import logging


def create_app():
    from app.routes.camera_routes import camera_blueprint

    app = Flask(__name__, template_folder='fhtml')
    app.register_blueprint(camera_blueprint)
    #basic configuration for message logs
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] %(message)s'
    )
    logger = logging.getLogger(__name__)

    #logging error handling exceptions
    @app.errorhandler(Exception)
    def handle_exception(e):
        logger.error(f'Unhandled eception: {e}', exc_info=True)
        return {"Error": str(e)}, 500

    return app
