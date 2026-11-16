import cv2

img = cv2.imread(r"C:\Users\VARSHINI\Downloads\images-7.jpeg")

threshold_value = 127

ret, segmented = cv2.threshold(
    img, threshold_value, 255,
    cv2.THRESH_BINARY
)

cv2.imshow("Original Image", img)
cv2.imshow("Segmented Image", segmented)

cv2.waitKey(0)
cv2.destroyAllWindows()
