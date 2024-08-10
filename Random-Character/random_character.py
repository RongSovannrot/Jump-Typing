import pygame
import string
import random
pygame.init()

#Display and Icon
pygame.init()
dis = pygame.display.set_mode((800, 330))
pygame.display.set_caption('Typing')

#backgournd
image_bg = pygame.image.load('Mario_bg.jpg')
image_bg = pygame.transform.scale(image_bg,(800,330))

#box
image_box = pygame.image.load('Box.png')
image_box = pygame.transform.scale(image_box,(37,37))
x_box = 810

#play34
player_image = pygame.image.load('icon.png')
player_image = pygame.transform.scale(player_image, (40,40))

#random character
chars = string.ascii_letters
print(chars)
random_string=random.choice(chars)
# render character
font = pygame.font.Font('freesansbold.ttf', 25)
if random_string == random_string.upper():
    text = font.render(random_string, True, (224, 224, 224))
elif random_string == random_string.lower():
    text = font.render(random_string, True, (160, 160, 160))
text_rect = text.get_rect(center=(x_box + image_box.get_width() // 2, 95 + image_box.get_height() // 2))
print(text_rect)

run = True
FPS = 60
clock = pygame.time.Clock()
while run:

    #bg
    dis.blit(image_bg, (0,0))

    #the moving of box
    x_box -= 5
    if x_box < 0:
        x_box = 810
    dis.blit(image_box, (x_box,95))

    #player icon
    dis.blit(player_image,(37,215))

 # random text
    if x_box == 810:
        random_string = random.choice(chars)
        if random_string == random_string.upper():
            text = font.render(random_string, True, (224, 224, 224))
        elif random_string == random_string.lower():
            text = font.render(random_string, True, (160, 160, 160))
    text_rect = text.get_rect(center=(x_box + image_box.get_width() // 2, 95 + image_box.get_height() // 2))
    print(text_rect)
    dis.blit(text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(FPS)
    pygame.display.update()