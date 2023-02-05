import cv2
from findBalloon import *
from detectHit import *
import threading
from game import *
from detectBall import *


def start_opencv():
    global balloonGame
    vid = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    count = 0
    while (True):
        # Capture the video frame
        # by frame
        ret, img = vid.read()
        cv2.imshow('Original', img)

        # imgBallons, balloonBoxes, ballBoxes = findBalloons(img)
        # frames = detectHit(img, balloonBoxes)
        ballCoordinates = detectBall(img)
        for coordinates in ballCoordinates:
            balloonGame.x_ball, balloonGame.y_ball = coordinates
        
        # cv2.imshow('Modified', imgBallons)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()



x_ball, y_ball = -1, -1
openCv = threading.Thread(target=start_opencv)
openCv.start()
balloonGame = Game()
balloonGame.start_game()