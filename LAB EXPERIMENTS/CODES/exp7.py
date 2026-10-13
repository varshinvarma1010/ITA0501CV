import cv2

video_path = r"C:\Users\VARSHINI\Downloads\sample video.mp4"

for mode in ["Normal Speed", "Slow Motion", "Fast Motion"]:
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Video not found!")
        break

    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30

    delay = {
        "Normal Speed": int(1000 / fps),
        "Slow Motion": int(2000 / fps),
        "Fast Motion": int(500 / fps)
    }[mode]

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Resize frame while maintaining aspect ratio
        height, width = frame.shape[:2]
        max_width = 800
        max_height = 600

        scale = min(max_width / width, max_height / height)

        new_width = int(width * scale)
        new_height = int(height * scale)

        frame = cv2.resize(frame, (new_width, new_height))

        cv2.imshow(mode, frame)

        if mode == "Fast Motion":
            cap.set(
                cv2.CAP_PROP_POS_FRAMES,
                cap.get(cv2.CAP_PROP_POS_FRAMES) + 1
            )

        if cv2.waitKey(max(1, delay)) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
