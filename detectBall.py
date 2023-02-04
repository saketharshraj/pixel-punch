import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# change resolution based on dslr input
# cap.set(3, 1280)
# cap.set(4, 720)

r, frame = cap.read()

# print('Resolution: ' + str(frame.shape[0]) + ' x ' + str(frame.shape[1]))

prevCircle = None
def dist(x1, y1, x2, y2): return (x1-x2)**2+(y1-y2)**2

while(True):
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)

    # change all the parameter values to adjust the circle detection sensitivity 
    # according of the ball dimenstions and the environment variables
    circles = cv.HoughCircles(blurred, cv.HOUGH_GRADIENT,
                               1.2, 50, param1=100, param2=30, minRadius=25, maxRadius=50)

    if circles is not None:
        
        circles = np.uint16(np.around(circles))
        chosen = None

        for i in circles[0, :]:
            if chosen is None:
                chosen = i
            if prevCircle is not None:
                if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= dist(i[0], [1], prevCircle[0], prevCircle[1]):
                    chosen = i
        
        cv.circle(frame, (chosen[0], chosen[1]), 1, (0, 100, 100), 3)
        cv.circle(frame, (chosen[0], chosen[1]), chosen[2], (255, 0, 255), 3)
        prevCircle = chosen


        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            cv.circle(frame, (x, y), 1, (0, 0, 255), 3)

            # prints coordinates of circle center            
            print("(",x, ",", y,")")

    cv.imshow("Frame", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    
cap.release()
cv.destroyAllWindows()