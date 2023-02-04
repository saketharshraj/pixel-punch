from findBalloon import *

def detectHit(img, bboxs):
    # Add crop image if needed
    # img = cropImage(img, 0.1)
    imgBallonList = splitBallons(img, bboxs)
    # showBallons(imgBallonList)
    frameWithBall = findBallInBallon(imgBallonList)
    return frameWithBall


def splitBallons(img, bboxs):
    imgBallonList = []
    for b in bboxs:
        x1,y1,x2,y2 = b[0], b[1], b[0]+b[2], b[1]+b[3]
        imgBallonList.append(img[y1:y2, x1:x2]) 
    return imgBallonList


def showBallons(imgBallonList):
    for (index, balloon) in enumerate(imgBallonList):
        cv2.imshow(f'Ballon {index}', balloon)



def findBallInBallon(imgBallonList):
    frameWithBall = []
    for i in range(len(imgBallonList)):
        img = imgBallonList[i]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply GaussianBlur to reduce noise
        gray = cv2.GaussianBlur(gray, (5, 5), 0)

        # Detect circles in the image using HoughCircles
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=30, minRadius=25, maxRadius=30)

        # If circles are detected, draw them on the original image
        if circles is not None:
            circles = np.uint16(np.around(circles))
            frameWithBall.append(imgBallonList[i])
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                cv2.circle(img, (x, y), r, (0, 255, 0), 3)
        # cv2.imshow(f"Circles {i}", img)

    # Display the image with circles
    # cv2.imshow("Circles", img)


        
    # just for rendering
    # for i in range(len(imgBallonList)):
    #     cv2.imshow(f'Ballon {i}', imgBallonList[i])

    return frameWithBall


