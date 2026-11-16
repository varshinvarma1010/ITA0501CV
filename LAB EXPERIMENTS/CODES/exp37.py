import cv2
import numpy as np

img = cv2.imread(r"C:\Users\VARSHINI\Downloads\sample image.png")

if img is None:
    print("Image not found!")
    exit()

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Select foreground color range
lower = np.array([35, 40, 40])
upper = np.array([85, 255, 255])

mask = cv2.inRange(hsv, lower, upper)

result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Original Image", img)
cv2.imshow("Foreground Extracted", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
