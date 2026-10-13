import cv2

def analyze_histogram(image):
    colors = ('b', 'g', 'r')

    for i, color in enumerate(colors):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        print(color.upper(), "channel:")
        print("Minimum:", histogram.min())
        print("Maximum:", histogram.max())

img = cv2.imread(r"C:\Users\VARSHINI\Downloads\sample image.png")

if img is None:
    print("Image not found!")
    exit()

analyze_histogram(img)
