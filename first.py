import pygame
import sys
import random
from math import *
import time

pygame.init()

width = 1300
height = 600

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("CopyAssignment - Balloon Shooter Game")
clock = pygame.time.Clock()

margin = 0
lowerBound = 150

score = 0

white = (230, 230, 230)
lightBlue = (4, 27, 96)
red = (231, 76, 60)
lightGreen = (25, 111, 61)
darkGray = (40, 55, 71)
darkBlue = (64, 178, 239)
green = (35, 155, 86)
yellow = (244, 208, 63)
blue = (46, 134, 193)
purple = (155, 89, 182)
orange = (243, 156, 18)

Img = pygame.image.load(r"pic.png")
Img = pygame.transform.scale (Img, (300, 300))

font = pygame.font.SysFont("Arial", 25)

class Balloon:
    def __init__(self, speed):
        self.a = 35
        self.b = self.a
        self.x = random.randrange(margin, width - self.a - margin)
        self.y = height - lowerBound
        self.angle = 90
        self.speed = -speed
        self.proPool= [-1]
        self.length = random.randint(50, 100)
        self.color = lightGreen
        
    def move(self):
        # direct = random.choice(self.proPool)

        # if direct == -1:
        #     self.angle += -10
        # elif direct == 0:
        #     self.angle += 0
        # else:
        #     self.angle += 10

        self.y += self.speed*1
        # self.x += self.speed*cos(radians(self.angle))

        if (self.x + self.a > width) or (self.x < 0):
            if self.y > height/5:
                self.x += self.speed*cos(radians(self.angle)) 
            else:
                self.reset()
        if self.y + self.b < 0 or self.y > height + 30:
            self.reset()
            
    def show(self):
        pygame.draw.line(display, darkBlue, (self.x + self.a/2, self.y + self.b), (self.x + self.a/2, self.y + self.b + self.length))
        pygame.draw.ellipse(display, self.color, (self.x, self.y, self.a, self.b))
        # pygame.draw.ellipse(display, self.color, (self.x + self.a/2 - 5, self.y + self.b - 3, 10, 10))
        # display.blit(Img, (self.x, self.y))


    def burst(self):
        global score
        pos = pygame.mouse.get_pos()

        if isonBalloon(self.x, self.y, self.a, self.b, pos):
            score += 1
            self.reset()
                
    def reset(self):
        self.a = random.randint(30, 40)
        self.b = self.a + random.randint(0, 10)
        self.x = random.randrange(margin, width - self.a - margin)
        self.y = height - lowerBound 
        self.angle = 90
        self.speed -= 0.002
        self.proPool = [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]
        self.length = random.randint(50, 100)
        self.color = lightGreen
       
balloons = []
noBalloon = 3
for i in range(noBalloon):
    obj = Balloon(1)
    balloons.append(obj)

def isonBalloon(x, y, a, b, pos):
    if (x < pos[0] < x + a) and (y < pos[1] < y + b):
        return True
    else:
        return False
    
def pointer():
    pos = pygame.mouse.get_pos()
    r = 25
    l = 20
    color = lightGreen
    for i in range(noBalloon):
        if isonBalloon(balloons[i].x, balloons[i].y, balloons[i].a, balloons[i].b, pos):
            color = red
    pygame.draw.ellipse(display, color, (pos[0] - r/2, pos[1] - r/2, r, r), 4)
    pygame.draw.line(display, color, (pos[0], pos[1] - l/2), (pos[0], pos[1] - l), 4)
    pygame.draw.line(display, color, (pos[0] + l/2, pos[1]), (pos[0] + l, pos[1]), 4)
    pygame.draw.line(display, color, (pos[0], pos[1] + l/2), (pos[0], pos[1] + l), 4)
    pygame.draw.line(display, color, (pos[0] - l/2, pos[1]), (pos[0] - l, pos[1]), 4)

def lowerPlatform():
    pygame.draw.rect(display, darkGray, (0, height - lowerBound, width, lowerBound))
    
def showScore():
    scoreText = font.render("Balloons Bursted : " + str(score), True, white)
    display.blit(scoreText, (150, height - lowerBound + 50))

def showLevel1():
    levelText = font.render("Level : 1", True, white)
    display.blit(levelText, (150, height - lowerBound + 0))

def showLevel2():
    levelText = font.render("Level : 2", True, white)
    display.blit(levelText, (150, height - lowerBound + 0))

def showLevel3():
    levelText = font.render("Level : 3", True, white)
    display.blit(levelText, (150, height - lowerBound + 0))

def close():
    pygame.quit()
    sys.exit()
    
def game():
    global score
    loop = True
    start = time.time()

    while loop:
        
        total = round((time.time() - start), 2)
        timeText = font.render("Time: " + str(total), True, white)
        

        if(total == 30):
            close()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    score = 0
                    game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(noBalloon):
                    balloons[i].burst()

        display.fill(lightBlue)
        
        for i in range(noBalloon):
            balloons[i].show()

        pointer()
        
        for i in range(noBalloon):
            balloons[i].move()

        
        lowerPlatform()
        showScore()
        
        
        if(score <= 15):
            clock.tick(100)
            showLevel1()
        elif(15<score<25):
            clock.tick(225)
            showLevel2()
        elif(25<=score):
            clock.tick(350)
            showLevel3()

        display.blit(timeText, (150, height - lowerBound + 100))
        pygame.display.update()
game()