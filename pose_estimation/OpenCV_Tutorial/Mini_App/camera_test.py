from app.classes.camera import Camera
import cv2
#50A5DC2AA5BB
cam = Camera('http://192.168.0.29:4747/video')
capture = cam.show_screen()
#capture
key = cv2.waitKey(0)
