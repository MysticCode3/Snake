import pygame
from threading import Timer
import time
import random

#Width and Height of window
widthW = 20
heightW = 40

totalWH = widthW * heightW

# snake

#Velocity for player
vel = widthW

#Detects position of mouse click
cx, cy = (0, 0)

direction = None

freeze = False

cycleTime = 0.00000000000000000000000001

left = False
right = False
up = False
down = False

pygame.init()


def cycle():
    global direction
    global cycleTime
    if direction == 'left':
        s.moveLeft()
        Timer(cycleTime, cycle).start()

def cycle1():
    global direction
    global cycleTime
    if direction == 'right':
        s.moveRight()
        Timer(cycleTime, cycle1).start()

def cycle2():
    global direction
    global cycleTime
    if direction == 'up':
        s.moveUp()
        Timer(cycleTime, cycle2).start()

def cycle3():
    global direction
    global cycleTime
    if direction == 'down':
        s.moveDown()
        Timer(cycleTime, cycle3).start()

class Fruit():
    xFruit, yFruit = 0, 0
    fruitE = 0
    def __init__(self, xFruit, yFruit, fruitE):
        self.xFruit, yFruit, fruitE = xFruit, yFruit, fruitE
        self.ifColide = False
        self.points = 0

    def drawFruit(self):
        if self.fruitE == 0:
            self.fruitE = 1
            self.xFruit = random.randint(0, widthW - 1)
            self.yFruit = random.randint(0, heightW - 1)
            self.xFruit = self.xFruit * totalWH/(totalWH/2)*10
            self.yFruit = self.yFruit * totalWH/(totalWH/2)*10
        #print(self.xFruit, self.yFruit)
        pygame.draw.rect(win, (255, 0, 0), (int(self.xFruit), int(self.yFruit), int(width), int(height)))
        #print(xFruit)
        #print(yFruit)

    def fruitCollision(self):
        xS = s.getSnakebodyX()
        yS = s.getSnakebodyY()
        snakeBody = s.getSnakeBody()
        #print(s.getSnakebodyX(), s.getSnakebodyY(), self.xFruit, self.yFruit)
        if xS == self.xFruit:
            if yS == self.yFruit:
                self.fruitE = 0
                self.ifColide = True
        if self.ifColide == True:
            self.points += 1
            self.ifColide = False
            spart = snakePiece(xS, yS + vel)
            snakeBody.insert(len(snakeBody), spart)
            #print(snakeBody)
        else:
            pass

    def collide(self):
        return self.ifColide

    def point(self):
        return self.points

class snakePiece():
    x, y = 0, 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return int(self.x)

    def getY(self):
        return int(self.y)

    def moveLeft(self):
        self.x = self.x - vel

    def moveRight(self):
        self.x = self.x + vel

    def moveUp(self):
        self.y = self.y - vel

    def moveDown(self):
        self.y = self.y + vel


class snake():
    snakeBody = []

    def __init__(self):
        self.snakebody = None
        self.snakeBody.append(snakePiece(400, 400))
        self.snakeBody.append(snakePiece(400 + vel, 400))
        self.snakeBody.append(snakePiece(400 + 2 * vel, 400))
        #self.snakeBody.append(snakePiece(400 + 3 * vel, 400))
        #self.snakeBody.append(snakePiece(400 + 4 * vel, 400))
        self.lost = False

    def drawSnake(self):
        for i in range(0, len(self.snakeBody)):
            snakePart = self.snakeBody[i]
            pygame.draw.rect(win, (67, 84, 255), (snakePart.getX(), snakePart.getY(), int(width), int(height)))

    def moveLeft(self):
        time.sleep(0.1)
        spart = snakePiece(self.snakeBody[0].getX() - vel, self.snakeBody[0].getY())
        # if NO fruit eaten then run below
        self.snakeBody.pop()
        self.snakeBody.insert(0, spart)

    def moveRight(self):
        time.sleep(0.1)
        spart = snakePiece(self.snakeBody[0].getX() + vel, self.snakeBody[0].getY())
        self.snakeBody.pop()
        self.snakeBody.insert(0, spart)

    def moveUp(self):
        time.sleep(0.1)
        spart = snakePiece(self.snakeBody[0].getX(), self.snakeBody[0].getY() - vel)
        self.snakeBody.pop()
        self.snakeBody.insert(0,spart)

    def moveDown(self):
        time.sleep(0.1)
        spart = snakePiece(self.snakeBody[0].getX(), self.snakeBody[0].getY() + vel)
        self.snakeBody.pop()
        self.snakeBody.insert(0,spart)

    def collideWall(self):
        if self.snakeBody[0].getX() == 800:
            self.lost = True
        if self.snakeBody[0].getX() == -20:
            self.lost = True
        if self.snakeBody[0].getY() == -20:
            self.lost = True
        if self.snakeBody[0].getY() == 800:
            self.lost = True

    def getSnakebodyX(self):
        return self.snakeBody[0].getX()

    def getSnakebodyY(self):
        return self.snakeBody[0].getY()

    def getSnakeBody(self):
        return self.snakeBody

    def getdidLost(self):
        return self.lost

win = pygame.display.set_mode((totalWH, totalWH))
pygame.display.set_caption("Jumping Game 2")

width = totalWH/(totalWH/2)*10
height = totalWH/(totalWH/2)*10
run = True
s = snake()
F = Fruit(0, 0, 0)

    #Keeps the window running
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #Detects where the player clicks
        if event.type == pygame.MOUSEBUTTONUP:
            cx, cy = pygame.mouse.get_pos()
            print(cx, cy)

    keys = pygame.key.get_pressed()
        #Left and Right
    if freeze == False:
        if keys[pygame.K_LEFT]:
            if direction == 'right':
                pass
            else:
                if left == False:
                    left = True
                    right = False
                    up = False
                    down = False
                    direction = 'left'
                    cycle()
        if keys[pygame.K_RIGHT]:
            if direction == 'left':
                pass
            else:
                if right == False:
                    right = True
                    left = False
                    up = False
                    down = False
                    direction = 'right'
                    cycle1()
        if keys[pygame.K_UP]:
            if direction == 'down':
                pass
            else:
                if up == False:
                    up = True
                    left = False
                    right = False
                    down = False
                    direction = 'up'
                    cycle2()
        if keys[pygame.K_DOWN]:
            if direction == 'up':
                pass
            else:
                if down == False:
                    down = True
                    left = False
                    right = False
                    up = False
                    direction = 'down'
                    cycle3()

    #Colors
    greenColor = 150, 200, 20
    blueColor = 67, 84, 255
    orangeColor = 255, 165, 0
    redColor = 250, 0, 0
    purpleColor = 172, 79, 198
    grayColor = 128, 128, 128

    #Generates Font
    font = pygame.font.SysFont("comicsans", 40)
    fontBig = pygame.font.SysFont("comicsans", 50)
    fontSmall = pygame.font.SysFont("comicsans", 26)
    # Fills the screen with black
    win.fill((greenColor))
    #Draws Player
    #pygame.draw.rect(win, (150, 200, 20), (int(x), int(y), int(width), int(height)))

    points = F.point()
    didLose = s.getdidLost()

    pointsLabel = font.render(str(points), bool(1), (255, 255, 255))
    win.blit(pointsLabel, (10, 10))
    if didLose == True:
        lost = font.render("You Lost", bool(1), (255, 255, 255))
        win.blit(lost, (335, 400))
        totalPoint = font.render(f"Total Points: {points}", bool(1), (255, 255, 255))
        win.blit(totalPoint, (300, 450))
        freeze = True
        cycleTime = 100000

    F.fruitCollision()
    s.drawSnake()
    s.collideWall()
    F.drawFruit()

    pygame.display.update()

pygame.quit()