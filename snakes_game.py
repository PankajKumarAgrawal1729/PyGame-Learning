import pygame
import random

pygame.init()

screenWidth = 900
screenHeight = 600

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
gameWindow = pygame.display.set_mode((screenWidth, screenHeight))

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




def gameLoop():
    # game variable
    exitGame = False
    gameOver = False
    snakeX = 55
    snakeY = 45
    initialVelocity = 10
    velocityX = 0
    velocityY = 0
    foodX = random.randint(20, screenWidth / 2)
    foodY = random.randint(20, screenHeight / 2)
    blockSize = 10
    fps = 30
    score = 0
    snakeList = []
    snakeLength = 1
    with open("highScore.txt", "r") as f:
        highScore = f.read()

    while not exitGame:
        if gameOver:
            with open("highScore.txt", "w") as f:
                f.write(str(highScore))
            gameWindow.fill(white)
            printScore("Game Over! Press Enter to Play Again", red,  100, 200)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitGame = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameLoop()
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
            snakeX += velocityX
            snakeY += velocityY

            if abs(snakeX - foodX) < 6 and abs(snakeY - foodY) < 6:
                score += 10
                foodX = random.randint(20, screenWidth / 2)
                foodY = random.randint(20, screenHeight / 2)
                snakeLength += 5
                if score > int(highScore):
                    highScore = score
                
            # fill color in screen
            gameWindow.fill(white)
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


gameLoop()
pygame.quit();
quit()
