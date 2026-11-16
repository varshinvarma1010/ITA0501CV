import cv2
import numpy as np

width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

img = np.ones((height, width, 3), dtype=np.uint8) * 255

cv2.rectangle(img, (100, 100), (width-100, height-100),
              (0, 0, 255), 3)

cv2.imshow("Rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
