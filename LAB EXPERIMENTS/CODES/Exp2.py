import cv2

img = cv2.imread(r"C:\Users\VARSHINI\Downloads\sample image.jpeg")

if img is None:
    print("Image not found!")
    exit()

blur = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imshow("Original Image", img)
cv2.imshow("Blur Image", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
