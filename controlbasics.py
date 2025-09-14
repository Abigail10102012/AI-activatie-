import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open webcam")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define skin color range in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Create a binary mask where skin color areas are white
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Apply mask to original frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(max_contour) > 500:
            x, y, w, h = cv2.boundingRect(max_contour)

            # Calculate center of the contour
            center_x = x + w // 2
            center_y = y + h // 2

            # Draw a circle at
