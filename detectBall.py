import cv2
import numpy as np


def detectBall(frame):    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Use the HoughCircles function to detect circles in the grayscale image
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=15, maxRadius=25)
    
    ballCoordinates = []
    # Check if the HoughCircles function has detected any circles
    if circles is not None:
        # Convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        
        # Loop through the circles and draw a circle around each one
        for (x, y, r) in circles:
            ballCoordinates.append((x, y))
            # cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
            # cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            # print(f'{x}, {y}, {r}')
    
    return ballCoordinates
