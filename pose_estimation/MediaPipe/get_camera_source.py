import cv2

def get_camera_source():
    # 1️⃣ Try native webcam
    for idx in range(5):  # scan first 5 possible indices
        cap = cv2.VideoCapture(idx)
        if cap.isOpened():
            print(f"[INFO] Using native webcam index {idx}")
            return cap

    # 2️⃣ Try DroidCam network stream
    urls = ["http://droidcam.local:4747/video", "http://192.168.1.50:4747/video"]
    for url in urls:
        cap = cv2.VideoCapture(url)
        if cap.isOpened():
            print(f"[INFO] Using DroidCam stream {url}")
            return cap

    # 3️⃣ Prompt user for MP4 file
    filepath = input("No camera found. Please provide a .mp4 file path: ")
    if filepath.endswith(".mp4"):
        cap = cv2.VideoCapture(filepath)
        if cap.isOpened():
            print(f"[INFO] Using video file {filepath}")
            return cap

    # Fail if nothing works
    raise RuntimeError("No camera or valid video file found!")

# Usage
cap = get_camera_source()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Camera / Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()