"""this script contains unit tests of all class methods"""
from app.classes.camera import Camera
from app.classes.user import User

def run_user_tests():
    print('Beginning tests for creation of users.')
    first_user = User(first_name='Kevin', last_name='Sanchez', height=180, weight=190)
    second_user = User(first_name='Joseph', last_name='Gleason', height=187.0, weight=223)
    third_user = User(first_name='Jean', last_name='Carrion', height=178, weight=210)
    fourth_user = User(first_name='Sean', last_name='Cardona', height=188, weight=165)

    print(first_user.to_dict())
    print(second_user.to_dict())
    print(third_user.to_dict())
    print(fourth_user.to_dict())

run_user_tests()

def run_class_camera():
    print('Displaying camera class and its methods')
    cam = Camera(0)
    print(dir(cam))
    print('Displaying class methods na ddictionary annotatino')
    print('Test complete.')

run_class_camera()