import cv2
import numpy as np

def findBallInBallon():

    img1 = cv2.imread('./resources/circle.jpg')
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray, 5)
    cimg = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2BGR)

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=30, minRadius=20, maxRadius =70)
    
    circles  = np.uint16(np.around(circles))
       
    for i in circles[0,: ]:
        cv2.circle(img1, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(img1, (i[0], i[1]), 2, (0, 255, 0), 3)
    cv2.imshow('detected circles', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

findBallInBallon()
