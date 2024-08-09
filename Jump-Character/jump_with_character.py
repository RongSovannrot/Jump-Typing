import pygame
from pygame.locals import*
import random
import string
import math

#Start pygame
pygame.init()
dis = pygame.display.set_mode((800, 330))
pygame.display.set_caption('Typing')

#Icon
img_icon = pygame.image.load('icon (2).png')
pygame.display.set_icon(img_icon)

# Background
image_bg = pygame.image.load('Mario_bg.jpg')
image_bg = pygame.transform.scale(image_bg, (800,330))
# Make background a lives
bg_width = image_bg.get_width()
bg_height = image_bg.get_height()
t_width = math.ceil(800 / bg_width) + 1
t_height = math.ceil(330 / bg_height)
lives = 0

#box
image_box = pygame.image.load('Box.png')
image_box = pygame.transform.scale(image_box,(37,37))
x_box = 810

# Player
player_img = pygame.image.load('icon.png')
player_img = pygame.transform.scale(player_img, (40, 40))
# player jump
p_x, p_y = 100, 220
jump = False
y_g = 1
j_h = 15
y_v = j_h

#random character
length = 1
chars = string.ascii_letters
random_string = random.choice(chars)
# render character
font = pygame.font.Font('freesansbold.ttf', 30)
if random_string == random_string.upper():
    text = font.render(random_string, True, (224, 224, 224))
elif random_string == random_string.lower():
    text = font.render(random_string, True, (160, 160, 160))
text_rect = text.get_rect(center=(x_box + image_box.get_width() // 2, 95 + image_box.get_height() // 2))

# alphabet key
key_map = {
    'lower_letter': {
        pygame.K_a: 'a', pygame.K_b: 'b', pygame.K_c: 'c', pygame.K_d: 'd', pygame.K_e: 'e', pygame.K_f: 'f',
        pygame.K_g: 'g', pygame.K_h: 'h', pygame.K_i: 'i', pygame.K_j: 'j', pygame.K_k: 'k', pygame.K_l: 'l',
        pygame.K_m: 'm', pygame.K_n: 'n', pygame.K_o: 'o', pygame.K_p: 'p', pygame.K_q: 'q', pygame.K_r: 'r',
        pygame.K_s: 's', pygame.K_t: 't', pygame.K_u: 'u', pygame.K_v: 'v', pygame.K_w: 'w', pygame.K_x: 'x',
        pygame.K_y: 'y', pygame.K_z: 'z',
    },
    'upper_letter': {
        pygame.K_a: 'A', pygame.K_b: 'B', pygame.K_c: 'C', pygame.K_d: 'D', pygame.K_e: 'E', pygame.K_f: 'F',
        pygame.K_g: 'G', pygame.K_h: 'H', pygame.K_i: 'I', pygame.K_j: 'J', pygame.K_k: 'K', pygame.K_l: 'L',
        pygame.K_m: 'M', pygame.K_n: 'N', pygame.K_o: 'O', pygame.K_p: 'P', pygame.K_q: 'Q', pygame.K_r: 'R',
        pygame.K_s: 'S', pygame.K_t: 'T', pygame.K_u: 'U', pygame.K_v: 'V', pygame.K_w: 'W', pygame.K_x: 'X',
        pygame.K_y: 'Y', pygame.K_z: 'Z'
    }
}

run = True
clock = pygame.time.Clock()
FPS   = 60

while run:
       # player Jump
    keys = pygame.key.get_pressed()
    for key_upper, value_upper in key_map['upper_letter'].items():
        mod = pygame.key.get_mods()
        if value_upper == random_string and keys[key_upper] and mod & pygame.KMOD_SHIFT:
            jump = True
    for key_lower, value_lower in key_map['lower_letter'].items():
        if value_lower == random_string and keys[key_lower] and mod & pygame.KMOD_SHIFT:
            jump = False
        elif value_lower == random_string and keys[key_lower]:
            jump = True

    #jump position
    if jump:
        p_y -= y_v
        y_v -= y_g
        if y_v < -j_h:
            jump = False
            y_v = j_h
        print("X= ", p_x)
        print("Y= ", p_y)

    #random text
    random_string=random.choice(chars)
    if x_box == 810:
        if random_string == random_string.upper():
            text = font.render(random_string, True, (224, 224, 224))
        elif random_string == random_string.lower():
            text = font.render(random_string, True, (160, 160, 160))
        text_rect = text.get_rect(center=(x_box + image_box.get_width() // 2, 95 + image_box.get_height() // 2))
    text_rect = text.get_rect(center=(x_box + image_box.get_width() // 2, 95 + image_box.get_height() // 2))
    text_rect.center = (x_box + image_box.get_width() // 2, 95 + image_box.get_height() // 2)
    dis.blit(text, text_rect)

    #background
    for i in range(0, t_width):
        dis.blit(image_bg, (i * bg_width + lives, 0))
    lives -= 5
    if abs(lives) > bg_width:
        lives = 0
    # player
    dis.blit(player_img, (p_x, p_y))

    #the moving of box
    x_box -= 5
    if x_box < 0:
        x_box = 810
    dis.blit(image_box, (x_box,95))

    # text position
    text_rect.center = (x_box + image_box.get_width() // 2, 95 + image_box.get_height() // 2)
    dis.blit(text, text_rect)

    # End game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    clock.tick(FPS)
    pygame.display.update()
pygame.quit()
