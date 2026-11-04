
import cv2

img = cv2.imread(r"C:\Users\VARSHINI\Downloads\sample image.png")

watermarked = img.copy()

cv2.putText(
    watermarked,
    "MY WATERMARK",
    (30, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

cv2.imshow("Original Image", img)
cv2.imshow("Watermarked Image", watermarked)

cv2.imwrite("watermarked.jpg", watermarked)

cv2.waitKey(0)
cv2.destroyAllWindows()

