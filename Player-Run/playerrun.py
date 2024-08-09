import pygame
import math
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

#player
player_image = pygame.image.load('icon.png')
player_image = pygame.transform.scale(player_image,(40,40))

run = True
FPS = 60
clock = pygame.time.Clock()
print("i    i*bg_width  lives   i*bg_width+lives")
while run:
    for i in range(0, t_width):
        dis.blit(bg,(i*bg_width+lives,0))
        print(i,"\t",i*bg_width,"\t",lives,"\t",i*bg_width+lives)
    lives-=5
    if -1*lives>bg_width:
        lives=0

    dis.blit(player_image,(37,220))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    clock.tick(FPS)
    pygame.display.flip()