import cv2
import numpy as np

# Load the image
img = cv2.imread('./resources/100.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect circles in the image using HoughCircles
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=30, minRadius=20, maxRadius=200)

# If circles are detected, draw them on the original image
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)

# Display the image with circles
cv2.imshow("Circles", img)
cv2.waitKey(0)
