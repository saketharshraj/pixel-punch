import cv2
import numpy as np


def findBalloons(img):

    # Below crop was used to remove headers from the video
    # img = cropImage(img, 0.1)

    # some pre processing on image to make it ready to find contours
    img = preProcess(img)

    # find contours and ballon boxes
    img, balloonBoxes, ballBoxes = findContours(img)
    return (img, balloonBoxes, ballBoxes)


def cropImage(img, cropVal):
    h, w, c = img.shape
    img = img[int(cropVal*h):h, 0:w]
    return img


def preProcess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (5, 5), 5, 0)
    img = cv2.Canny(img, 50, 100)
    kernel = np.ones((5, 5), np.uint8)
    img = cv2.dilate(img, kernel)
    return img


def findContours(img):

    
    balloonBoxes = []
    ballBoxes = []

    h, w = img.shape
    imgContours = np.zeros((h, w), np.uint8)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

    for i, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        if area > 30000 and area < 250000:
            cv2.drawContours(imgContours, contours, i, (255, 0, 255), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(imgContours, (x,y), (x+w, y+h), (255,0,255), 2)
            balloonBoxes.append([x, y, w, h])
        else:
            x, y, w, h = cv2.boundingRect(cnt)
            ballBoxes.append([x, y, w, h])

    return (imgContours, balloonBoxes, ballBoxes)


