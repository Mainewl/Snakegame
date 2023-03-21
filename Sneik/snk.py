import pygame
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dsp_w = 600
dps_h = 400
 
dis = pygame.display.set_mode((dsp_w, dps_h))
pygame.display.set_caption('Sneik')
 
clock = pygame.time.Clock()
 
snk_bck = 10
snk_spd = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("", 25)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])
 
 
 
def our_snake(snk_bck, snk_list):
    for x in snk_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snk_bck, snk_bck])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dsp_w / 6, dps_h / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dsp_w / 2
    y1 = dps_h / 2
 
    x1_change = 0
    y1_change = 0
 
    snk_list = []
    lng_snk = 1
 
    foodx = round(random.randrange(0, dsp_w - snk_bck) / 10.0) * 10.0
    foody = round(random.randrange(0, dps_h - snk_bck) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(lng_snk - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snk_bck
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snk_bck
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snk_bck
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snk_bck
                    x1_change = 0
 
        if x1 >= dsp_w or x1 < 0 or y1 >= dps_h or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snk_bck, snk_bck])
        snk_head = []
        snk_head.append(x1)
        snk_head.append(y1)
        snk_list.append(snk_head)
        if len(snk_list) > lng_snk:
            del snk_list[0]
 
        for x in snk_list[:-1]:
            if x == snk_head:
                game_close = True
 
        our_snake(snk_bck, snk_list)
        Your_score(lng_snk - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dsp_w - snk_bck) / 10.0) * 10.0
            foody = round(random.randrange(0, dps_h - snk_bck) / 10.0) * 10.0
            lng_snk += 1
 
        clock.tick(snk_spd)
 
    pygame.quit()
    quit()
 
 
gameLoop()