import cv2

img = cv2.imread(r"C:\Users\VARSHINI\Downloads\sample image.png")

rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
