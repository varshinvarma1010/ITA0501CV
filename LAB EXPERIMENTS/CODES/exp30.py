import cv2

img = cv2.imread(r"C:\Users\VARSHINI\Downloads\images-7.jpeg")

if img is None:
    print("Image not found!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

smiles = smile_cascade.detectMultiScale(
    gray,
    scaleFactor=1.5,
    minNeighbors=20,
    minSize=(25, 15)
)

if len(smiles) > 0:
    # Select only the largest detected smile
    x, y, w, h = max(smiles, key=lambda r: r[2] * r[3])

    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    print("Smile Detected")
else:
    print("Smile Not Detected")

cv2.imshow("Smile Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
