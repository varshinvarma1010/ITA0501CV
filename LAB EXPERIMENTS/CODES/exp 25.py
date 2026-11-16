import cv2
import numpy as np

# Load input image
img = cv2.imread(r"C:\Users\VARSHINI\Downloads\sample image.png")

# Load MobileNet SSD model
prototxt = "MobileNetSSD_deploy.prototxt"
model = "MobileNetSSD_deploy.caffemodel"

net = cv2.dnn.readNetFromCaffe(prototxt, model)

# Object classes
classes = [
    "background", "aeroplane", "bicycle", "bird",
    "boat", "bottle", "bus", "car", "cat", "chair",
    "cow", "diningtable", "dog", "horse", "motorbike",
    "person", "pottedplant", "sheep", "sofa",
    "train", "tvmonitor"
]

# Prepare image
blob = cv2.dnn.blobFromImage(
    cv2.resize(img, (300, 300)),
    0.007843, (300, 300), 127.5
)

net.setInput(blob)

# Detect objects
detections = net.forward()

count = 0

for i in range(detections.shape[2]):

    confidence = detections[0, 0, i, 2]

    if confidence > 0.40:

        index = int(detections[0, 0, i, 1])

        if classes[index] == "bird":

            count += 1

            box = detections[0, 0, i, 3:7] * np.array([
                img.shape[1], img.shape[0],
                img.shape[1], img.shape[0]
            ])

            x1, y1, x2, y2 = box.astype("int")

            cv2.rectangle(
                img, (x1, y1), (x2, y2),
                (0, 255, 0), 2
            )

            cv2.putText(
                img, "Bird",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 0), 2
            )

print("Number of Birds Detected:", count)

cv2.imshow("Bird Recognition", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
