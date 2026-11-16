import cv2

cap = cv2.VideoCapture(r"C:\Users\VARSHINI\Downloads\video.mp4")

frames = []

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

if len(frames) == 0:
    print("Video not found!")
    exit()

height, width, _ = frames[0].shape

out = cv2.VideoWriter(
    "reverse.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    20,
    (width, height)
)

for frame in reversed(frames):
    out.write(frame)

out.release()

print("Reverse video created successfully!")

# Play the reversed video
cap = cv2.VideoCapture("reverse.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Reverse Video", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
