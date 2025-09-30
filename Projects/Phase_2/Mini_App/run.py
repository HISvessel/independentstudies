"""this is the file in which the app will be run"""
from app import create_app

app = create_app()

def main():
    app.run()