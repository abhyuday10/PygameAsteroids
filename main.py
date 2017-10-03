import Ship_File
import Shot
import asteroids
import os
import pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"



screen = pygame.display.set_mode(Ship_File.screen_size)
pygame.display.set_caption("ASTEROIDS")

clock = pygame.time.Clock()



def main_run():
    screenWidth, screenheight = Ship_File.screen_size[0],Ship_File.screen_size[1]
    gameRunning = True

    clock,ship = Ship_File.main_setup()
    rockList, score, clock = asteroids.main_setup(screenWidth, screenheight)

    while gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False
        screen.fill((0, 0, 0))
        Ship_File.main_loop(screen,ship,clock)
        asteroids.newGame(screenWidth,screenheight,screen,rockList,score,clock,ship)

main_run()