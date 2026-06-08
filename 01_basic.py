import pygame

pygame.init()

# Creating Window
gameWindow = pygame.display.set_mode((1200, 500))

# Adding title for window
pygame.display.set_caption("My First Game")


# Game Specific variables
exit_game = False
game_over = False


# Creating a game loop
while not exit_game :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("Right Pressed")

pygame.quit()
quit()