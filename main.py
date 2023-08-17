# importing pygame
import pygame

# initializate pygame
pygame.init()

# window size
screen_width = 800
screen_height = 600

# size constant
SIZE = (screen_width, screen_height)

# icon variable
icon = pygame.image.load("./Space_Invaders/spaceship.png")
pygame.display.set_icon(icon)

# title of the window
pygame.display.set_caption("Space invaders")
# Bg image
background_img = pygame.image.load("Space_Invaders/sstronomy2.png")

# display of the window
screen = pygame.display.set_mode(SIZE)

# Player function
player_img = pygame.image.load("./Space_Invaders/spaceship.png")
player_x = 370
player_y = 480
player_x_change = 0
player_y_change = 0

def player(x,y):
    screen.blit(player_img, (x,y))

# Game loop

running = True
while running == True:
    for event in pygame.event.get():
        # Event to close the window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_a:
                  player_x_change = -0.5
              if event.key == pygame.K_d:
                  player_x_change = 0.5

              if event.key == pygame.K_w:
                  player_y_change = -0.5
              if event.key == pygame.K_s:
                  player_y_change = 0.5
        if event.type == pygame.KEYUP:
               if event.key == pygame.K_a:
                    player_x_change = 0
               if event.key == pygame.K_d:
                    player_x_change = 0
               if event.key == pygame.K_w:
                    player_y_change = 0
               if event.key == pygame.K_s:
                    player_y_change = 0

    # Background blit
    screen.blit(background_img, (0,0))

    # player movements
    player_x += player_x_change
    player_y += player_y_change
    # Player blit
    player(player_x,player_y)

    pygame.display.flip()
pygame.quit()