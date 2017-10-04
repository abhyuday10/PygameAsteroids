from math import *
def rad_to_offset(radians, offset):  # insert better func name.
    x = cos(radians) * offset
    y = sin(radians) * offset
    return [x, y]

import pygame
class projectile:
    def __init__(self,angle,position):
        self.angle = angle
        shot_position = position
        second =[0,0]
        second[0] = shot_position[0] + rad_to_offset(angle, 1)[0]
        second[1] = shot_position[1] + rad_to_offset(angle, 1)[1]
        self.point1 = position
        self.point2 = second
        print("AHHHHA",rad_to_offset(angle, 1)[1])

    def move(self):
        self.point1[0] += rad_to_offset(self.angle, 1)[0]
        self.point1[1] -= rad_to_offset(self.angle, 1)[1]
        self.point2[0] += rad_to_offset(self.angle, 1)[0]
        self.point2[1] -= rad_to_offset(self.angle, 1)[1]

    def draw(self,surface):
        pygame.draw.line(surface, (255, 255, 255), self.point1,self.point2, True)


