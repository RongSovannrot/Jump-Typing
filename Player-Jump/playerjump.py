import pygame
from pygame.locals import*
import math

#Start pygame
pygame.init()
dis = pygame.display.set_mode((800, 330))
pygame.display.set_caption('Typing')

#Icon
img_icon = pygame.image.load('icon (2).png')
pygame.display.set_icon(img_icon)

# Background
bg = pygame.image.load('Mario_bg.jpg')
bg_width = bg.get_width()
bg_height = bg.get_height()
print(bg_width)
#Make background a lives
t_width = math.ceil(800 / bg_width)+1
t_height = math.ceil(330 / bg_height)
lives = 0

# Player
player_img = pygame.image.load('icon.png')
player_img = pygame.transform.scale(player_img, (40, 40))
# player jump
p_x = 100
p_y = 220
jump = False
y_g = 1
y_h = 15
y_v = y_h

run = True
clock = pygame.time.Clock()
FPS   = 60
while run:

    # bg move
    for i in range(0, t_width):
        dis.blit(bg,(i*bg_width+lives,0))
    lives-=5
    if -1*lives>bg_width:
        lives=0
    #player jump
    if jump:
        p_y -= y_v
        y_v -= y_g
        if y_v < -15:
            jump = False
            y_v = y_h
    dis.blit(player_img, (p_x, p_y))

    # End game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN:
            jump = True
    clock.tick(FPS)
    pygame.display.update()
pygame.quit()
