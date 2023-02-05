import pygame
import cv2
import numpy as np
import threading


class Game:
    def __init__(self) -> None:
        # Load the assets
        self.balloon_img = pygame.image.load("./resources/balloon_purple.png")

        # calliberation coordinates
        # self.topLeft = None
        # self.topRight = None
        # self.bottomLeft = None
        # self.bottomRight = None

        # list of calliberation coordinates
        self.coordinates = []


        # Set up the game window
        self.window_size = (1200, 700)
        self.screen = pygame.display.set_mode(self.window_size)

        # Calliberate
        self.dots = []

        pygame.init()
    

    def start_calliberation(self):
        black = (0, 0, 0)
        green = (0, 255, 0)
        # Game loop
        running = True
        while running:
            print(True)
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    self.dots.append(pos)
                  

            for dot in self.dots:
                pygame.draw.circle(self.screen, green, dot, 20, 0)
                
            
            pygame.display.update()
            

        # Quit Pygame
        pygame.quit()



def startCircleDetection():  
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply GaussianBlur to reduce noise
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Use the HoughCircles function to detect circles in the grayscale image
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=15, maxRadius=25)
        
        calliberateCircleCoordinates = []
        # Check if the HoughCircles function has detected any circles
        if circles is not None:
            # Convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
            
            # Loop through the circles and draw a circle around each one
            for (x, y, r) in circles:
                calliberateCircleCoordinates.append((x, y))
                cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
                print(f'{x}, {y}, {r}')
        cv2.imshow('Frame', frame)
        # if len(calliberateCircleCoordinates) == 4:
        #     break


if __name__ =="__main__":
    game = Game()
    # calliberation = Calliberate()

    calliberationGame = threading.Thread(target=game.start_calliberation)
    
    # openCv = threading.Thread(target=calliberation.startCircleDetection)

    calliberationGame.start()
    # openCv.start()

    # game.start_calliberation()
    
    # startCircleDetection()
    
