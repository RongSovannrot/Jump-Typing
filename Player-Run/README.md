# Player Run
It is really important in this Typing Jump for running of Player.
## Implement Code
First, we should prompt all nessary varable to handle it in display like their posiiton, shape like this.
### Code
    import pygame
    import math
    pygame.init()
    dis = pygame.display.set_mode((800, 330))
    pygame.display.set_caption('Typing')
So we imported pygame and math. We use it to handle our process, espacailly pygame which is a library to make game or somthing else.
##### pygame.intit()
This is a important part of pygame because it is like a brain.
##### pygame.display.set_mode()
This attribute is used to set the size of our display.
In this context we set it to variable dis.
##### pyame.display.set_caption()
This is used to set title of game.
## Background
To make Player Run, we make the background move instead, because when Player is moving so the bg is immobile so it is not interesting.
But bg moving is more intesting than Player moving.
### Code
    bg = pygame.image.load('Mario_bg.jpg')
    bg_width = bg.get_width()
    bg_height = bg.get_height()
So these code we handle the image into display and we have to find the width of bg for mesuring that how many of bg to fill the display, because the size of display is bigger than bg.
#####  bg_width = bg.get_width()
This is used to find the length of width. Anyway bg_height is the same and is not nescessary.
## Background Move Implement
These code is used to masure how many bg to fill display size
#### Code
    t_width = math.ceil(800 / bg_width)+1
    t_height = math.ceil(330 / bg_height)
    lives = 0
##### math.ceil()
This is used to change the value from floating to digit.
## Player
In this context, this section is not important, so put it in display or not, don't care. This code is use to handle player in display.
### Code
    #player
    player_image = pygame.image.load('icon.png')
    player_image = pygame.transform.scale(player_image,(40,40))
## Veloceity
This is important to setting the veloceity, if not we can not watch becasue it is really fast. This section connect to frame. So, we setting it to slowdown the frame in While loop.
    FPS = 60
    clock = pygame.time.Clock()
##### pygame.time.Clock()
To massure frame.
## Graphic of Pygame
This section we use while loop to make our display load until we quit it. So it loads becasue of frame. We can say, event in pygame.
    run = True
    while run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
So this code it is useful to quit the game.
##### pygame.display.flip() or pygame.display.update()
You see this code right. So this code is used to update all process, like when we want to make it move or add any attribute we have to mention it. It is up to date.
## How Bg Moving
    for i in range(0, t_width):
        dis.blit(bg,(i*bg_width+lives,0))
    lives-=5
    if -1*lives>bg_width:
        lives=0
    dis.blit(player_image,(37,220))
This code makes bg move cause player run.
