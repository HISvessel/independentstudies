from app.classes.camera import Camera
import cv2


cam = Camera(source='http://192.168.0.9:4747/video')
print('Beginning test for camera object')
capture = cam.video_camera()
while True:
    success, frames = cam.capture_frames(capture)
    if not success:
        print('Error capturing frames')
        break
    cam.display_window(frames)
    if cam.exit_key() & 0XFF == ord('q'):
        print('Ending loop')
        break
cam.release_window(capture)
print('Window closed gracefully. Testing complete')
