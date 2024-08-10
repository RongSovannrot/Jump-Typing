# Random Character
In this section, we random character by using random library. So we should import random.
The character have to put in the box to make the user clear which letter should they type to make it jump.
When the box is moving so the character is also moving.
## Character
We store all alphabet and random it
### Code
    chars = string.ascii_letters
    random_string=random.choice(chars)
#### string.ascii_letters
This is used to store all alphabet. We set it to variable chars.
#### random.choice(chars)
This is uesed to random. This context our computer will random one of all alphabet and store it in variable random_string.
## Render character
We render the character, it make user easy to play to notice which character is lower or upper.
We set, if character is white so it is upper, otherwise is lower.
### Code
    font = pygame.font.Font('freesansbold.ttf', 25)
    if random_string == random_string.upper():
        text = font.render(random_string, True, (224, 224, 224))
    elif random_string == random_string.lower():
        text = font.render(random_string, True, (160, 160, 160))
#### pygame.font.Font()
This is used to set font of letters.
#### font.render()
This is used to customize colour of letters.
## letter in Box
We put our letter in the Box and make it in the center.
### Code
#### text_rect = text.get_rect(center=(x_box + image_box.get_width() // 2, 95 + image_box.get_height() // 2))
This code is used to make it in center and attribute cneter is used to make sure it is in center.
## In While Loop
Anyway we also process it in while loop.
### Code
    chars = string.ascii_letters
    random_string=random.choice(chars)
    font = pygame.font.Font('freesansbold.ttf', 25)
    if random_string == random_string.upper():
        text = font.render(random_string, True, (224, 224, 224))
    elif random_string == random_string.lower():
        text = font.render(random_string, True, (160, 160, 160))
    text_rect = text.get_rect(center=(x_box + image_box.get_width() // 2, 95 + image_box.get_height() // 2))
#### So we have to put it one more time in while loop. To make it continue to random until end event.
