import cv2
import pytesseract

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

cap = cv2.VideoCapture(r"C:\Users\VARSHINI\Downloads\video1.mp4")

if not cap.isOpened():
    print("Video not found!")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame into grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Extract text
    text = pytesseract.image_to_string(gray)

    if text.strip():
        print("Extracted Text:")
        print(text)

    cv2.imshow("Video", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
