import pygame
import time
import random
import math
from word import vocabulary_list
################################################
width = 600
height = 650
center = (300,325)
screen = pygame.display.set_mode((width, height))
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
################################################
menu_sound = False
game_over_sound = False
game_sound = False
story = False
intro_sound = False
################################################
################### BUTTON #####################
start = pygame.image.load('Pics/button/start.png')
start_click = pygame.image.load('Pics/button/startclick.png')
exit_ = pygame.image.load('Pics/button/exit.png')
exit_click = pygame.image.load('Pics/button/exitclick.png')
credit = pygame.image.load('Pics/button/credit.png')
credit_click = pygame.image.load('Pics/button/creditclick.png')
howto = pygame.image.load('Pics/button/howtoplay.png')
howto_click = pygame.image.load('Pics/button/howtoplayclick.png')
################################################
game_bg = pygame.image.load('Pics/game_bg.jpg')
################### GHOST ######################
g1 = pygame.image.load('Pics/Ghost/1.png')
g2 = pygame.image.load('Pics/Ghost/2.png')
g3 = pygame.image.load('Pics/Ghost/3.png')
g4 = pygame.image.load('Pics/Ghost/4.png')
g5 = pygame.image.load('Pics/Ghost/5.png')
g6 = pygame.image.load('Pics/Ghost/6.png')
g7 = pygame.image.load('Pics/Ghost/7.png')
g8 = pygame.image.load('Pics/Ghost/8.png')
g9 = pygame.image.load('Pics/Ghost/9.png')
g10 = pygame.image.load('Pics/Ghost/10.png')
g11 = pygame.image.load('Pics/Ghost/11.png')
g12 = pygame.image.load('Pics/Ghost/12.png')
################### HEART ######################
h3 = pygame.image.load('Pics/Heart/heart3.png')
h2 = pygame.image.load('Pics/Heart/heart2.png')
h1 = pygame.image.load('Pics/Heart/heart1.png')
################### DANGER ######################
dan1 = pygame.image.load('Pics/danger/red1.png')
dan2 = pygame.image.load('Pics/danger/red2.png')
################### COLOR ######################
black = (0, 0, 0)
white = (255, 255, 255)
################################################
# TEXT SHOW
def text_objects(text, font, color=None):
    if not color:
        color = black
    textsurface = font.render(text, True, color)
    return textsurface, textsurface.get_rect()

def show_message(text, size, position, color=None, fontfam=None):
    if not color:
        color = black
    if not fontfam:
        #fontfam = None
        fontfam = "fonts/FIPPS___.ttf"
    sizetext = pygame.font.Font(fontfam, size)
    textsurface, textrec = text_objects(text, sizetext, color)
    textrec.center = position
    screen.blit(textsurface, textrec)
    
# GHOST ANIMATION
def ghost(x,y,n):
    if n < 1:
        screen.blit(g1, (x-55, y-100))
        n += 0.4
    elif n < 2:
        screen.blit(g2, (x-55, y-100))
        n += 0.4
    elif n < 3:
        screen.blit(g3, (x-55, y-100))
        n += 0.4
    elif n < 4:
        screen.blit(g4, (x-55, y-100))
        n += 0.4
    elif n < 5:
        screen.blit(g5, (x-55, y-100))
        n += 0.4
    elif n < 6:
        screen.blit(g6, (x-55, y-100))
        n += 0.4
    elif n < 7:
        screen.blit(g7, (x-55, y-100))
        n += 0.4
    elif n < 8:
        screen.blit(g8, (x-55, y-100))
        n += 0.4
    elif n < 9:
        screen.blit(g9, (x-55, y-100))
        n += 0.4
    elif n < 10:
        screen.blit(g10, (x-55, y-100))
        n += 0.4
    elif n < 11:
        screen.blit(g11, (x-55, y-100))
        n += 0.4
    elif n < 12:
        screen.blit(g12, (x-55, y-100))
        n += 0.4
        if n > 12:
            n = 0
    return n

# INTRO STORY
def intro():
    global story,intro_sound
    all_story = False
    if not story:
        all_story = []
        for img in range(1,8):
            all_story += [pygame.image.load('Pics/Story/' + str(img) + '.jpg')]
    first_scene = True
    break_story = True
    last_scene = False
    if not intro_sound:
        intro_sound = pygame.mixer.Sound('Sound/intro.wav')
        intro_sound.set_volume(.2)
        intro_sound.play()  
    if all_story:
        while break_story:
            slide = 40
            try:
                if first_scene:
                    story = all_story.pop(0)
                    first_scene = False
                else:
                    story = all_story.pop(0)
            except:
                last_scene = True
            while slide < 255:
                slide += 10
                story.set_alpha(slide)
                screen.blit(story, (0, 0))
                pygame.time.delay(70)
                pygame.display.update()
            screen.blit(story, (0, 0))
            if last_scene:
                break_story = False
            pygame.display.update()
            
# GAME TO PLAY                          
def game():
    menu_sound.stop()
    intro()
    intro_sound.stop()
    global game_sound ,game_over_sound 
    if not game_sound :
        game_sound = pygame.mixer.Sound('Sound/POL-final-act-short.wav')
        game_sound.set_volume(.2)
        game_sound.play(loops = - 1)
        
    # PLAY GAME OVER SOUND 
    game_over_sound = False

    # SET SILEN SOUND
    silen = pygame.mixer.Sound('Sound/silen.wav')
    silen.set_volume(.7)
    
    # CALL VOCABULARY
    list_word = vocabulary_list()

    danger = 0
    show_ = 0
    
    life = 3
    score = 0
    
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0

    # MOVE TEXT
    speed_max = 5
    speed_min = 3

    speed_1 = random.randrange(speed_min,speed_max)
    speed_2 = random.randrange(speed_min,speed_max)
    speed_3 = random.randrange(speed_min,speed_max)
    speed_4 = random.randrange(speed_min,speed_max)

    # SHOW AND CHECK WORD
    w1 = ''
    w2 = ''
    w3 = ''
    w4 = ''

    w_check = ''
    show_input = ''

    # POSITION
    x1 = 155
    x2 = 235
    x3 = 355
    x4 = 435

    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0
    
    # RANDOM SPEED MOVE
    random_speed = random.randrange(0, 99)* 0.001
    # SET A TO Z ON SHOW MESSAGE
    A_TO_Z = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    # SET KEYBOARD
    KEY = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m,
              pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, 13, pygame.K_BACKSPACE, '''pygame.K_ESCAPE''', pygame.K_SPACE]

    while True:
        # CLEAR SCREEN
        if list_word == []:
            list_word = word_list()
            
        # BG GAME
        screen.fill(0)
        screen.blit(game_bg, (0, 0))
        
        # CHECK LIFE
        if life == 3:
            screen.blit(h3, (0, 0))

        if life == 2:
            screen.blit(h2, (0, 0))

        if life == 1:
            screen.blit(h1, (0, 0))

        if life == 0:
            AH = pygame.mixer.Sound('Sound/AHHHH.wav')
            AH.set_volume(.3)
            AH.play()
            game_over()
            if life > 0:
                game_over()

        # SHOW SCORE    
        show_message(str(score), 20, (525, 30),
                    white,  "fonts//FIPPS___.ttf")
        
        # MOVE PICS WITH TEXT
        n1 = ghost(x1+30,y1,n1)
        n2 = ghost(x2+30,y2,n2)
        n3 = ghost(x3+30,y3,n3)
        n4 = ghost(x4+30,y4,n4)
        
        # SHOW TEXT W1 - W4
        if w1 == '':
            show_w1 = list_word.pop(0)
            i = 0
            for j in show_w1:
                index = A_TO_Z.index(j)
                if w1 == '':
                    w1 += str(KEY[index])
                    i = 1
                else:
                    w1 += '.' + str(KEY[index])
        show_message(show_w1, 22, (x1, y1),white, "fonts//theboldfont.ttf")

        if w2 == '':
            show_w2 = list_word.pop(0)
            i = 0
            for j in show_w2:
                index = A_TO_Z.index(j)
                if w2 == '':
                    w2 += str(KEY[index])
                    i = 1
                else:
                    w2 += '.' + str(KEY[index])
        show_message(show_w2, 22, (x2, y2),white, "fonts//theboldfont.ttf")

        if w3 == '':
            show_w3 = list_word.pop(0)
            i = 0
            for j in show_w3:
                index = A_TO_Z.index(j)
                if w3 == '':
                    w3 += str(KEY[index])
                    i = 1
                else:
                    w3 += '.' + str(KEY[index])
                       
        show_message(show_w3, 22, (x3, y3),white, "fonts//theboldfont.ttf")

        if w4 == '':
            show_w4 = list_word.pop(0)
            i = 0
            for j in show_w4:
                index = A_TO_Z.index(j)
                if w4 == '':
                    w4 += str(KEY[index])
                    i = 1
                else:
                    w4 += '.' + str(KEY[index])
        show_message(show_w4, 22, (x4, y4),white, "fonts//theboldfont.ttf")

        # LOOP GAME
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if (event.type == pygame.KEYDOWN and event.key in KEY):
                '''if event.key == pygame.K_ESCAPE:
                    pass'''
                if event.key == pygame.K_BACKSPACE:
                    w_check = w_check.split('.')
                    del w_check[-1]
                    w_check = ".".join(w_check)
                    continue
                elif event.key == pygame.K_SPACE or event.key == 13:
                    # IF CORRECT
                    if w1 ==  w_check or w2 ==  w_check or w3 ==  w_check or w4 ==  w_check:
                        score += 1
                        if  w_check != '':
                            output =  w_check.split('.')
                            for i in output:
                             i = int(i) - 97
                             show_input += A_TO_Z[i]
                             wing = pygame.mixer.Sound('Sound/wing.wav')
                             wing.set_volume(.5)
                             wing.play()
                            show_input = ''
                            
                        if w1 == w_check:
                            w1 = ''
                            y1 = 0
                            x1 = 155
                            speed_1 = 0
                            speed_1 = random.randrange(speed_min,speed_max)

                        elif w2 == w_check:
                            w2 = ''
                            y2 = 0
                            x2 = 235
                            speed_2 = 0
                            speed_2 = random.randrange(speed_min,speed_max)

                        elif w3 == w_check:
                            w3 = ''
                            y3 = 0
                            x3 = 355
                            speed_3 = 0
                            speed_3 = random.randrange(speed_min,speed_max)

                        elif w4 == w_check:
                            w4 = ''
                            y4 = 0
                            x4 = 435
                            speed_4 = 0
                            speed_4 = random.randrange(speed_min,speed_max)
                        w_check = ''
                    else :
                        wrong = pygame.mixer.Sound('Sound/wrong.wav')
                        wrong.set_volume(.5)
                        wrong.play()
                        pygame.display.update()
                        w_check = ''

                else :
                    if w_check == '':
                        w_check += str(event.key)
                    else :
                         w_check += "." + str(event.key)
        # NOT CORRECT
        if w_check != '':
            output = w_check.split('.')
            for i in output:
                i = int(i) - 97
                show_input += A_TO_Z[i]
                
        # SHOW INPUT       
        show_message(show_input, 30, (315, 560),
                    black,  "fonts//FIPPS___.ttf")
        show_input = ''

        # RUN NEW TEXT
        # IF CORRECT
        if y1 > 415:
            w1 = ''
            life -= 1
            x1 = 155
            y1 = 0

        if y2 > 417:
            w2 = ''
            life -= 1
            x2 = 235
            y2 = 0

        if y3 > 419:
            w3 = ''
            life -= 1
            x3 = 355
            y3 = 0

        if y4 > 421:
            w4 = ''
            life -= 1
            x4 = 435
            y4 = 0
            
        # LEVEL UP SPEED  
        if score >= 30 :
            y1 += (speed_1 * random_speed + 0.1)*2
            y2 += (speed_2 * random_speed + 0.2)*2
            y3 += (speed_3 * random_speed + 0.1)*2
            y4 += (speed_4 * random_speed + 0.3)*2
            if y1 > 390 or y2 > 390 or y3 > 390 or y4 > 390:
                silen_check = True
                if danger == 0:
                    screen.blit(dan1, (0, 0))
                    danger = 1
                elif danger == 1:
                    screen.blit(dan2, (0, 0))
                    danger = 2
                elif danger == 2:
                    screen.blit(dan1, (0, 0))
                    danger = 3
                elif danger == 3:
                    screen.blit(dan2, (0, 0))
                    danger = 0
            else:
                silen_check = False
                sound = True
                        

        # LEVEL UP SPEED 2
        if score >= 90:
            y1 += (speed_1 * random_speed + 0.1)*3
            y2 += (speed_2 * random_speed + 0.2)*3
            y3 += (speed_3 * random_speed + 0.1)*3
            y4 += (speed_4 * random_speed + 0.3)*3
            if y1 > 390 or y2 > 390 or y3 > 390 or y4 > 390:
                silen_check = True
                if danger == 0:
                    screen.blit(dan1, (0, 0))
                    danger = 1
                elif danger == 1:
                    screen.blit(dan2, (0, 0))
                    danger = 2
                elif danger == 2:
                    screen.blit(dan1, (0, 0))
                    danger = 3
                elif danger == 3:
                    screen.blit(dan2, (0, 0))
                    danger = 0
            else:
                silen_check = False
                sound = True
        
        # CKECK DANGER ZONE
        if y1 > 390 or y2 > 390 or y3 > 390 or y4 > 390:
            silen_check = True
            if danger == 0:
                screen.blit(dan1, (0, 0))
                danger = 1
            elif danger == 1:
                screen.blit(dan2, (0, 0))
                danger = 2
            elif danger == 2:
                screen.blit(dan1, (0, 0))
                danger = 3
            elif danger == 3:
                screen.blit(dan2, (0, 0))
                danger = 0
        else:
            silen_check = False
            sound = True

        # IF DANGER ZONE PLAY SOUND
        if silen_check and sound:
            silen.play()
            sound = False
        if sound:
            silen.stop()
            sound = True

        # LOOP SPEED TEXT
        y1 += speed_1 * random_speed + 0.1
        y2 += speed_2 * random_speed + 0.2
        y3 += speed_3 * random_speed + 0.1
        y4 += speed_4 * random_speed + 0.3
     
        pygame.display.update()
        clock.tick(30)
   
# BUUTON
def button(icon,icon_click,x,y,w,h,order = None, p = None):
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if p:
        x1 = x + w + 10
        x2 = x - 10
        y1 = y + h
        y2 = y - 10
    else:
        x1 = x + w + 10
        x2 = x - 10
        y1 = y + h - 10
        y2 = y - 10
    if (x1 > mouse[0] > x2) and (y1 > mouse[1] > y2):
        screen.blit(icon_click, (x , y))
        click_sound = pygame.mixer.Sound('Sound/button.wav') 
        if click[0] == 1 and order is not None:
            click_sound.set_volume(.1)
            click_sound.play(loops =  1)
            if order == 'exit':
                pygame.quit()
                quit()
            if order == 'start':
                game()
            if order == 'howto':
                hot_to_play()
            if order == 'credit':
                credit_()
    else:
        if p:
            screen.blit(icon, (x , y))
        else:
            screen.blit(icon, (x , y ))


### HOW TO PLAY ###
def hot_to_play():
    slide = 40
    howto_ =  pygame.image.load('Pics/howtoplay.jpg')
    while True:
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()
        if slide < 255:
            slide += 10
            howto_.set_alpha(slide)
            screen.blit(howto_, (0, 0))
            pygame.time.delay(100)
        screen.blit(howto_, (0, 0))
        pygame.display.update()
        clock.tick(30)

### CREDIT ###
def credit_():
    slide = 40
    credit_ =  pygame.image.load('Pics/credit.png')
    while True:
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()
        if slide < 255:
            slide += 10
            credit_.set_alpha(slide)
            screen.blit(credit_, (0, 0))
            pygame.time.delay(100)
        screen.blit(credit_, (0, 0))
        pygame.display.update()
        clock.tick(30)
    
### GAME OVER ###
def game_over():
    game_sound.stop()
    global game_over_sound,menu_sound  
    slide = 40
    game_over_pic = pygame.image.load('Pics/gameover.jpg')
    if not game_over_sound:
        game_over_sound = pygame.mixer.Sound('Sound/menu_1.wav')
        game_over_sound.set_volume(.2)
        game_over_sound.play(loops = - 1)
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over_sound.stop()
                    # SET PLAY MENU SOUND
                    menu_sound = False
                    menu()
        if slide < 255:
            slide += 10
            game_over_pic.set_alpha(slide)
            screen.blit(game_over_pic, (0, 0))
            pygame.time.delay(100)
        screen.blit(game_over_pic, (0, 0))
        pygame.display.update()
        clock.tick(30)
    
### MENU GAME ###
def menu():
    global menu_sound,game_sound 
    slide = 40
    if not menu_sound :
        menu_sound = pygame.mixer.Sound('Sound/POL-spirits-dance-short.wav')
        menu_sound.set_volume(.2)
        menu_sound.play(loops=-1)
    Background = pygame.image.load('Pics/bg.jpg')
    while True:
        game_sound = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if slide < 255:
            slide += 10
            Background.set_alpha(slide)
            screen.blit(Background, (0, 0))
            pygame.time.delay(100)
            '''if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                print(mx,my)'''
        screen.blit(Background, (0, 0))
        button(start,start_click,200,240,130,130,'start')
        button(howto,howto_click,200,340,130,130,'howto')
        button(credit,credit_click,200,440,160,160,'credit')
        button(exit_,exit_click,200,540,160,160,'exit')
        pygame.display.update()
        clock.tick(30)
pygame.init()
pygame.display.set_caption("GHOST SKULL")
menu()
#game() ----> TEST GAME FUNCTION



