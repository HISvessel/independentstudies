from app.classes.camera import Camera
import cv2
cam = Camera('http://192.168.0.3:4747/video')
print('Beginning test for camera object')
print('Step 1: Opening the camera lens')
capture = cam.video_camera()
while True:
    print('Step 2: Capturing frames')
    success, frames = cam.capture_frames(capture)
    print('Step 2 Success')
    if not success:
        print('Error capturing frames')
        break
    print('Step 3: Displaying captured frames in window')
    cam.display_window(frames)
    print('Step 4: closing window. Awaiting input....')
    if cam.exit_key() & 0XFF == ord('q'):
        print('Ending loop')
        break
cam.release_window(capture)
print('Window closed gracefully. Testing complete')
