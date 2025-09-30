from app.classes.threaded_cam import CameraThreaded
import cv2
import numpy as np
cam = CameraThreaded('http://192.168.0.9:4747/video')

while True:
    frame = cam.get_frame() #capturing regular frames
    encoded_bytes = cam.get_encoded_frame() #writing frames to bytecode

    #decoding bytecodes as a frame by frame read
    np_arr = cv2.imdecode(
        np.frombuffer(encoded_bytes, np.uint8),
        cv2.IMREAD_COLOR
    )
    if frame is None:
        continue  # wait until first frame is ready

    fps = cam.get_fps()
    cv2.putText(frame, f'FPS: {fps}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Live feed (Threaded)", frame)
    cv2.imshow('decoded frames', np_arr)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.stop()