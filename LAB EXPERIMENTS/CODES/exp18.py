
import cv2

img = cv2.imread(r"C:\Users\VARSHINI\Downloads\sample image.png")

roi = img[50:200, 50:200]

result = img.copy()

result[220:370, 220:370] = roi

cv2.imshow("Original Image", img)
cv2.imshow("Cropped ROI", roi)
cv2.imshow("Copied and Pasted Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

