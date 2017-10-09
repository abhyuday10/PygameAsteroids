import pygame
import os

os.environ["SDL_VIDEO_CENTERED"] = "1"


screen_size = [1000, 200]
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("ASTEROIDS")

clock = pygame.time.Clock()

A = [(0,0),(30,50),(60,0),(50,0),(30,15),(10,0),(0,0)]
Ain = [(30,55),(28,52),(32,52),(30,55)]

def asteroidstxt(screen,A,Ain):
    screen.fill((0, 0, 0))
    for i in range(len(A)-1):

        pygame.draw.line(screen, (255, 255, 255), A[i], A[i+1], True)



gameRunning = True

while gameRunning == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
        asteroidstxt(screen,A,Ain)
        pygame.display.flip()