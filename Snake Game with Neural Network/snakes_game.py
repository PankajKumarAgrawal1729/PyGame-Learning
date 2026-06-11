import pygame
import random
import os

pygame.init()



screenWidth = 900
screenHeight = 600
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HIGH_SCORE_FILE = os.path.join(BASE_DIR, "highScore.txt")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
gameWindow = pygame.display.set_mode((screenWidth, screenHeight))

#backgroundimage
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (screenWidth, screenHeight)).convert_alpha()  # to convert image to alpha format for better performance

pygame.display.set_caption("Snake Game")

#\
font = pygame.font.SysFont(None, 55)
clock = pygame.time.Clock()

def plotSnake(gameWindow, color, snakeList, blockSize):
    for x,y in snakeList:
        pygame.draw.rect(gameWindow, color, (x, y, blockSize, blockSize))

def printScore(text, color, x, y) :
    screenText = font.render(text, True, color)
    gameWindow.blit(screenText, [x, y])

def saveHighScore(highScore):
    with open(HIGH_SCORE_FILE, "w") as f:
        f.write(str(highScore))

def welcome() :
    exitGame = False
    while not exitGame:
        gameWindow.fill((233, 210, 229))
        printScore("Welcome to Snakes Game", red, 200, 200)
        printScore("Press Space Bar To Play", black, 200, 250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playGame()
        pygame.display.update()
        clock.tick(60)


def playGame():
    # game variable
    exitGame = False
    gameOver = False
    snakeX = 55
    snakeY = 45
    initialVelocity = 10
    velocityX = 0
    velocityY = 0
    foodX = random.randint(20, screenWidth // 2)
    foodY = random.randint(20, screenHeight // 2)
    blockSize = 10
    fps = 30
    score = 0
    snakeList = []
    snakeLength = 1

    # check if highScore.txt file exists, if not create one and write 0 in it
    if not os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "w") as f:
            f.write("0")
    with open(HIGH_SCORE_FILE, "r") as f:
        highScoreText = f.read().strip()
        highScore = int(highScoreText) if highScoreText else 0

    while not exitGame:
        if gameOver:
            saveHighScore(highScore)
            gameWindow.fill(white)
            printScore("Game Over! Press Enter to Play Again", red,  100, 200)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    saveHighScore(highScore)
                    exitGame = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitGame = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocityX = initialVelocity
                        velocityY = 0
                    if event.key == pygame.K_LEFT:
                        velocityX = -initialVelocity
                        velocityY = 0
                    if event.key == pygame.K_UP:
                        velocityX = 0
                        velocityY = -initialVelocity
                    if event.key == pygame.K_DOWN:
                        velocityX = 0
                        velocityY = initialVelocity
                    
                    # Cheat Code
                    if event.key == pygame.K_q:
                        score += 10
            snakeX += velocityX
            snakeY += velocityY

            if abs(snakeX - foodX) < 6 and abs(snakeY - foodY) < 6:
                score += 10
                foodX = random.randint(20, screenWidth // 2)
                foodY = random.randint(20, screenHeight // 2)
                snakeLength += 5
                if score > highScore:
                    highScore = score
                    saveHighScore(highScore)
                
            # fill color in screen
            gameWindow.blit(background, (0, 0))
            printScore("Score: " + str(score), red, 5, 5)
            printScore("High Score: " + str(highScore), red, 200, 5)
            # Creating snake
            # (windowName, color, tuple(x-xis, y-axis, width, height))
            pygame.draw.rect(gameWindow, red, (foodX, foodY, blockSize, blockSize))
            
            head = []
            head.append(snakeX)
            head.append(snakeY)
            snakeList.append(head)

            if len(snakeList) > snakeLength:
                del snakeList[0]

            if snakeX < 0 or snakeX > screenWidth or snakeY < 0 or snakeY > screenHeight or head in snakeList[:-1]:
                gameOver = True

            plotSnake(gameWindow, black, snakeList, blockSize)

        # to apply changes on screen
        pygame.display.update()
        clock.tick(fps)


welcome()
pygame.quit();
quit()
