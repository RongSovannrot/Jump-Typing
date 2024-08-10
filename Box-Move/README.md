# Box Move
It is really important to make the box is moving because it provide a smooth running of Player.
## Implement Box Code
We have to prompt all nesccessary point for starting box like, position box, shape of box.
### Code
    image_box = pygame.image.load('Box.png')
    image_box = pygame.transform.scale(image_box,(37,37))
    x_box = 810
#### pygame.image.load() 
This attribute is used to uploal image in display.
#### pygame.image.transform.scale() 
This attribute is used to shape the image. For this context I set it to (37,37) size.
## Work On While
To make it works we have to make it move in While run which run is True
### Code
    x_box -= 5
    if x_box < 0:
        x_box = 810
    dis.blit(image_box, (x_box,95))
#### x_box -= 5 
Mean x_box = x_box-5
So it is in While loop, x_box is calulated until encounter a condition
#### In if condition
We use it to make sure that when x_box < 0, so it is in if condition which make x_box = 810. Totally, when it is less than 0 the box will be in position x = 810 if we think of coordinate.
