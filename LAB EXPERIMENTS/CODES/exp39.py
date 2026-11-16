import cv2

cap = cv2.VideoCapture(r"C:\Users\VARSHINI\Downloads\sample video.mp4")

if not cap.isOpened():
    print("Video not found!")
    exit()

frames = []

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

# Reverse the frames
frames.reverse()

# Play in slow motion
for frame in frames:
    cv2.imshow("Reverse Slow Motion", frame)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
