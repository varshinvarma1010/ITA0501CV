import cv2
import numpy as np

img = cv2.imread(r"C:\Users\VARSHINI\Downloads\sample image.png")

if img is None:
    print("Image not found!")
    exit()

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Select background color range
lower = np.array([35, 40, 40])
upper = np.array([85, 255, 255])

mask = cv2.inRange(hsv, lower, upper)

# Remove selected background color
result = img.copy()
result[mask > 0] = (255, 255, 255)

cv2.imshow("Original Image", img)
cv2.imshow("Background Removed", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
