import pygame
class cursor:
    def __init__(self,screen_size):
        self.screen_size = screen_size
        self.pos = [[(screen_size[0] / 2.3)-10, (screen_size[1] / 2.3)],
               [(screen_size[0] / 2.3) - 30, (screen_size[1] / 2.3)-20],
               [(screen_size[0] / 2.3) - 30, (screen_size[1] / 2.3)+20]]
    def draw_cursor(self,screen):
        pygame.draw.line(screen, (255, 255, 255), self.pos[1], self.pos[0], True)
        pygame.draw.line(screen, (255, 255, 255), self.pos[2], self.pos[0], True)

    def move(self):
        if self.pos[0][1] == self.screen_size[1] / 2.3:
            self.pos = [[(self.screen_size[0] / 2.3) - 10, (self.screen_size[1] / 2.3) +40],
                   [(self.screen_size[0] / 2.3) - 30, (self.screen_size[1] / 2.3) + 20],
                   [(self.screen_size[0] / 2.3) - 30, (self.screen_size[1] / 2.3) + 60]]
        else:
            self.pos = [[(self.screen_size[0] / 2.3) - 10, (self.screen_size[1] / 2.3)],
                   [(self.screen_size[0] / 2.3) - 30, (self.screen_size[1] / 2.3) - 20],
                   [(self.screen_size[0] / 2.3) - 30, (self.screen_size[1] / 2.3) + 20]]

