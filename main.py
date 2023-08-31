# importing pygame
import pygame
# importing random
import random
# importing random
import math
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
player_img = pygame.image.load("./Space_Invaders/astronave2.png")
player_x = 370
player_y = 480
player_x_change = 0
player_y_change = 0
def player(x,y):
    screen.blit(player_img, (x,y))
# Enemy function
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_enemies = 8

for item in range(number_enemies):
     enemy_img.append(pygame.image.load("./Space_Invaders/ovni.png"))
     enemy_x.append(random.randint(0,720))
     enemy_y.append(random.randint(50, 150))
     enemy_x_change.append(0.8)
     enemy_y_change.append(40)
     def enemy(x,y):
          screen.blit(enemy_img[item], (x,y))

# Bullet function
bullet_img = pygame.image.load("./Space_Invaders/bala.png")
bullet_x = 0
bullet_y = 400
bullet_state = True
bullet_y_change = 10
bullet_x_change = 0
def fire (x,y):
     global bullet_state
     bullet_state = False
     screen.blit(bullet_img, (x + 16 , y + 16))
# Game loop
def is_collision(b_x, b_y, e_x, e_y):
     distance = math.sqrt((e_x - b_x)**2 + (e_y - b_y)**2)
     if distance < 27:
          return True
     else:
          return False
running = True
while running == True:
    for event in pygame.event.get():
        # Event to close the window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_a:
                  player_x_change = -0.9
              if event.key == pygame.K_d:
                  player_x_change = 0.9
              if event.key == pygame.K_SPACE and bullet_state == True:
                  bullet_x = player_x
                  bullet_state = False
              if event.key == pygame.K_w:
                  player_y_change = -0.9
              if event.key == pygame.K_s:
                  player_y_change = 0.9
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

    # Bullet blit
    

    if bullet_y <= 0:
         bullet_y = 480
         bullet_state = True

    if bullet_state == False:
        fire(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # player movements
    player_x += player_x_change
    player_y += player_y_change

    # Limites
    if player_x >=736:
         player_x = 736
    
    if player_x <=0:
         player_x = 0

    if player_y >=545:
         player_y = 545

    if player_y <=0:
         player_y = 0

    
    



    # Player blit
    player(player_x,player_y)

    # Enemy blit

    for item in range(number_enemies):
          enemy_x[item] += enemy_x_change[item]
          if enemy_x[item] <= 0:
               enemy_x_change[item] = 0.8
               enemy_y[item] += enemy_y_change[item]
          
          if enemy_x[item] >= 736:
               enemy_x_change[item] = -0.8
               enemy_y[item] += enemy_y_change[item]

          collision = is_collision(bullet_x,bullet_y,enemy_x[item],enemy_y[item])
          if collision:
               bullet_state = True
               bullet_y = 480
               enemy_x[item] = random.randint(0, 800)
               enemy_y[item] = random.randint(50, 150)


          enemy(enemy_x[item], enemy_y[item])



    pygame.display.flip()
pygame.quit()