import cv2
img = cv2.imread('./resources/10.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 5, 0)
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=100, minRadius=100, maxRadius =200)
print('Circle', circles)
