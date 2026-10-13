import cv2
import numpy as np

img = cv2.imread(r"C:\Users\VARSHINI\Downloads\sample image.png")

if img is None:
    print("Image not found")
else:
    kernel = np.ones((5, 5), np.uint8)
    eroded = cv2.erode(img, kernel, iterations=1)

    cv2.imshow("Original Image", img)
    cv2.imshow("Eroded Image", eroded)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
