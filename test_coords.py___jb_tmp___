import pygame
import os
import eztext

os.environ["SDL_VIDEO_CENTERED"] = "1"

screen_size = [1000, 200]

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("cords test")

pygame.init()

gameRunning = True
events = pygame.event.get()
txtbx = eztext.Input(maxlength=45, color=(255, 0, 0), prompt='type here: ')
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False


    txtbx.update(events)
    # blit txtbx on the sceen
    txtbx.draw(screen)
    # refresh the display
    pygame.display.flip()

    x1 = int(eztext.Input())
    y1 = int(eztext.Input())
    x2 = int(eztext.Input())
    y2 = int(eztext.Input())
    pygame.draw.line(screen, (255, 255, 255), (x,y), (x2,y2), True)


def main():
    # initialize pygame
    pygame.init()
    # create the screen
    screen = pygame.display.set_mode((640,240))
    # fill the screen w/ white
    screen.fill((255,255,255))
    # here is the magic: making the text input
    # create an input with a max length of 45,
    # and a red color and a prompt saying 'type here: '
    txtbx = eztext.Input(maxlength=45, color=(255,0,0), prompt='type here: ')
    # create the pygame clock
    clock = pygame.time.Clock()
    # main loop!

    while 1:
        # make sure the program is running at 30 fps
        clock.tick(30)

        # events for txtbx
        events = pygame.event.get()
        # process other events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # clear the screen
        screen.fill((255,255,255))
        # update txtbx
        txtbx.update(events)
        # blit txtbx on the sceen
        txtbx.draw(screen)
        # refresh the display
        pygame.display.flip()

