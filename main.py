import Ship_File

import asteroids
import Menu_Items
import os
import pygame

os.environ["SDL_VIDEO_CENTERED"] = "1"



screen = pygame.display.set_mode(Ship_File.screen_size)
pygame.display.set_caption("ASTEROIDS")



clock = pygame.time.Clock()
def Main_Menu(screen):
    screenWidth, screenheight = Ship_File.screen_size[0], Ship_File.screen_size[1]
    gameRunning = True

    clock, ship = Ship_File.main_setup(0,200)

    pygame.font.init()  # you have to call this at the start,
    myfont1 = pygame.font.SysFont('Times New Roman', 100)
    myfont = pygame.font.SysFont('Times New Roman', 40)
    textsurface1 = myfont1.render('ASTEROIDS', False, (255, 255, 255))
    textsurface2 = myfont.render('Start', False, (255, 255, 255))
    textsurface3 = myfont.render('High Scores', False, (255, 255, 255))
    gameRunning = True
    while gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False
        screen.fill((0, 0, 0))
        Ship_File.main_loop(screen, ship, clock)
        screen.blit(textsurface1, (Ship_File.screen_size[0] / 3.2, (Ship_File.screen_size[1] / 2.3) - 100))
        screen.blit(textsurface2, (Ship_File.screen_size[0] / 2.3, Ship_File.screen_size[1] / 2.3))
        screen.blit(textsurface3, (Ship_File.screen_size[0] / 2.3, (Ship_File.screen_size[1] / 2.3) + 40))
        pygame.display.flip()





def endscreen(screen,score):
    screen.fill((0, 0, 0))
    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface1 = myfont.render('GAME OVER', False, (255, 255, 255))
    textsurface2 = myfont.render('score: ' + str(score), False, (255, 255, 255))
    screen.blit(textsurface1, (Ship_File.screen_size[0]/2.3,Ship_File.screen_size[1]/2.3))
    screen.blit(textsurface2, (Ship_File.screen_size[0] / 2.3, (Ship_File.screen_size[1] / 2.3)+40))
    pygame.display.flip()

def main_run():
    screenWidth, screenheight = Ship_File.screen_size[0],Ship_File.screen_size[1]
    gameRunning = True
    clock,ship = Ship_File.main_setup(0,0)
    rockList, score, clock = asteroids.main_setup(screenWidth, screenheight)
    alive = True
    while gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False

        if alive == False:
            endscreen(screen,score)
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                return True
        else:
            screen.fill((0, 0, 0))
            Ship_File.main_loop(screen, ship, clock)
            score, alive = asteroids.Main_Loop(rockList, score, screen, screenWidth, screenheight, clock, ship)

Main_Menu(screen)
var = True
while var == True:
    var =main_run()