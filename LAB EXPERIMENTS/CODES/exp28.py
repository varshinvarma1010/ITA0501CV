import cv2

# Read input video
cap = cv2.VideoCapture(r"C:\Users\VARSHINI\Downloads\traffic_video.mp4")

# Create background subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Resize frame
    frame = cv2.resize(frame, (800, 600))

    # Apply background subtraction
    mask = bg_subtractor.apply(frame)

    # Remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Find contours
    contours, hierarchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # Detect vehicles
    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 1000:
            x, y, w, h = cv2.boundingRect(contour)

            # Draw rectangle around vehicle
            cv2.rectangle(frame, (x, y), (x+w, y+h),
                          (0, 255, 0), 2)

            # Display vehicle label
            cv2.putText(frame, "Vehicle", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (0, 0, 255), 2)

    # Display output
    cv2.imshow("Vehicle Detection", frame)
    cv2.imshow("Foreground Mask", mask)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
