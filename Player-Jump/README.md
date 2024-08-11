# Player Jump
How to make make player jump?
This section it relate to Player-Run
## Prompt to Jump
Jump is a feature of this game to play.
### Code
    p_x = 100
    p_y = 220
    jump = False
    y_g = 1 
    y_h = 15
    y_v = y_h
These variable is the prompt of player to jump
## Process
This process is used in while loop.
### Code
    if jump:
        p_y -= y_v
        y_v -= y_g
        if y_v < -15:
            jump = False
            y_v = y_h
    dis.blit(player_img, (p_x, p_y))
##### dis.blit()
We use this attribute to set the Player where should its position.
So this code is used to make our player jump. Anyway we have to type to process jumping. 
## Type To Jump
When we type any keyboard the player will jump.
### Code
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.KEYDOWN:
                jump = True
##### if event.type == pygame.KEYDOWN
This condition is used to make sure if the user typed.
##### event.type == pygame.KEYDOWN 
It mentioned key on keyboard to type. They type, the process is worked.
