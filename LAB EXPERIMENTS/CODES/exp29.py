import cv2

# Read input image
img = cv2.imread(r"C:\Users\VARSHINI\Downloads\images-7.jpeg")

if img is None:
    print("Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Load eye detector
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_eye.xml"
)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray, 1.1, 5
)

count = 0

for (x, y, w, h) in faces:

    # Draw face rectangle
    cv2.rectangle(
        img, (x, y), (x+w, y+h),
        (255, 0, 0), 2
    )

    # Extract upper part of face
    roi_gray = gray[y:y+h//2, x:x+w]
    roi_color = img[y:y+h//2, x:x+w]

    # Detect eyes
    eyes = eye_cascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.1,
        minNeighbors=8,
        minSize=(20, 20)
    )

    for (ex, ey, ew, eh) in eyes:

        # Draw rectangle around eyes
        cv2.rectangle(
            roi_color,
            (ex, ey),
            (ex+ew, ey+eh),
            (0, 255, 0), 2
        )

        count += 1

print("Number of Eyes Detected:", count)

cv2.imshow("Eye Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
