"""this is the file in which the app will be run"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', localhost=5000, debug=True)