from math import *
import copy
import os
def rad_to_offset(radians, offset):  # insert better func name.
    x = cos(radians) * offset
    y = sin(radians) * offset
    return [x, y]

import pygame
class projectile():
    def __init__(self,angle,position,screenheight,screeenwidth):
        self.screenheight = screenheight
        self.screenwidth = screeenwidth
        self.angle = copy.copy(angle)
        self.point1 = copy.copy(position)
        self.point2 = [position[0]+ rad_to_offset(self.angle, 3)[0],position[1]-rad_to_offset(self.angle, 3)[1]]
        pass
    #     self.angle = angle
    #     shot_position = copy.copy(position)
    #     second =[0,0]
    #     second[0] = shot_position[0] + 1
    #     second[1] = shot_position[0] + 1
    #     #print(second)
    #     self.point1 = position
    #     self.point2 = second
    #     #print(self.point1)
    #     #print("AHHHHA",rad_to_offset(angle, 1)[0])

    def move(self):
        pass
        self.point1[0] += rad_to_offset(self.angle, 10)[0]
        self.point1[1] -= rad_to_offset(self.angle, 10)[1]
        self.point2[0] += rad_to_offset(self.angle, 10)[0]
        self.point2[1] -= rad_to_offset(self.angle, 10)[1]

    def get_pos(self):
        return self.point1[0],self.point1[1]

    def draw(self,surface):
        pygame.draw.line(surface, (255, 255, 255), self.point1,self.point2, True)

    def killcheck(self, screen):
        inflatedScreen = screen.get_rect()
        if not inflatedScreen.collidepoint(self.point1):
            return True

    def on_screen(self):
        if self.point1[1]> self.screenheight:
            return True
        if self.point1[1]< 0:
            return True

        if self.point1[0]>self.screenwidth:
            return False
        if self.point1[0]<0:
            return False

        return True
