
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\VARSHINI\Downloads\sample image.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

x = cv2.convertScaleAbs(sobel_x)
y = cv2.convertScaleAbs(sobel_y)

result = cv2.addWeighted(x, 0.5, y, 0.5, 0)

cv2.imshow("Original Image", img)
cv2.imshow("Sobel Edge Detection", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
