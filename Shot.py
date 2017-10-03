import Ship_File
import pygame
class projectile:
    def __init__(self,angle,position):
        shot_angle = angle
        shot_position = position
        second =[0,0]
        second[0] = self.shot_position[0] + self.rad_to_offset(self.angle, 1)[0]
        second[1] = self.shot_position[1] + self.rad_to_offset(self.angle, 1)[1]
        point = [[position], [second]]


    def move(self):
        self.point[0][0] += self.rad_to_offset(self.angle, 1)[0]
        self.point[0][1] -= self.rad_to_offset(self.angle, 1)[1]
        self.point[1][0] += self.rad_to_offset(self.angle, 1)[0]
        self.point[1][1] -= self.rad_to_offset(self.angle, 1)[1]

    def draw(self,surface):
        pygame.draw.line(surface, (255, 255, 255), self.points[0],self.points[1], True)

