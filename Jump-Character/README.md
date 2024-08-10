# Jump with Character
We try to make it jump up to letter show in the box. How?
## Alphabet Key
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
#### In this section we have to store a dicitonary of key alphabet, like if we press key a so what it is value so its value is a. 
#### pygame.k_a mean key press, so key a and the value is a.
## In While Loop
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
#### This is the code to make it jump up to letters
#### pygame.key.get_pressed() we use it proecess when key is pressed. It is better than pygame.KEYDOWN.
#### pygame.key.get_mod() use to mentioned mod key like crt, shift...
#### for the first for loop in condition if. We set this condtion to allow user to type upper key up to letter in the box.
#### Second for loop in first condition we set jump is False becase it is lowwer letter showing. So if the type ctr, jump doesn't process.
#### Otherwise jumpt set to True.