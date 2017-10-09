def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.
    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return (qx, qy)



class Ship:
    shot = []

    def __init__(self, x,y):
        self.position = [x,y]
        # List of (angle,radius) pairs.
        self.rel_points = [[((screen_size[0]/2)-25), ((screen_size[1]/2)-25)], [((screen_size[0]/2)), ((screen_size[1]/2)+25)], [((screen_size[0]/2)+25), ((screen_size[1]/2)-25)], [((screen_size[0]/2)), ((screen_size[1]/2)-10)],[((screen_size[0]/2))-25, ((screen_size[1]/2)-25)]]
        self.centre = [(screen_size[0]/2),(screen_size[1]/2)]
        for i in range(len(self.rel_points)):
          self.rel_points[i][0] =self.rel_points[i][0]+self.position[0]
          self.rel_points[i][1] = self.rel_points[i][1] + self.position[1]

          self.centre = [(screen_size[0] / 2)+x, (screen_size[1] / 2)+y]

        self.xspeed = 0
        self.yspeed = 0

    def rad_to_offset(self,radians, offset):  # insert better func name.
        x = cos(radians) * offset
        y = sin(radians) * offset
        return [x, y]

    def rotate_point(self,arg):
        angle = self.get_angle()
        if arg == "up":

            self.centre[0] = self.centre[0] - math.sin(angle)
            print(self.centre[0])
            self.centre[1] = self.centre[1] - math.sin(angle)
            print(self.centre[1])

            for i in range(5):
                self.rel_points[i][1] = self.rel_points[i][1] - math.sin(angle)
                self.rel_points[i][0] = self.rel_points[i][0] - math.cos(angle)
        else:
            for i in range(5):
                self.rel_points[i][1] = self.rel_points[i][1] + math.sin(angle)
                self.rel_points[i][0] = self.rel_points[i][0] + math.cos(angle)
            self.centre[0] = self.centre[1] + math.sin(angle)
            self.centre[1] = self.centre[0] + math.sin(angle)

    def move_y(self):
        #Needs Speed, Position
        key = pygame.key.get_pressed()
        angle = self.get_angle()
        speed = self.yspeed

        if key[pygame.K_UP]:
            self.centre[0] += self.rad_to_offset(angle, self.yspeed)[0]
            self.centre[1] -= self.rad_to_offset(angle, self.yspeed)[1]
            for i in range(5):
                self.rel_points[i][0] += self.rad_to_offset(angle,self.yspeed)[0]
                self.rel_points[i][1] -= self.rad_to_offset(angle, self.yspeed)[1]
            self.yspeed += 0.3

        if key[pygame.K_DOWN]:
            self.centre[0] += self.rad_to_offset(angle, self.yspeed)[0]
            self.centre[1] -= self.rad_to_offset(angle, self.yspeed)[1]
            for i in range(5):
                self.rel_points[i][0] += self.rad_to_offset(angle, self.yspeed)[0]
                self.rel_points[i][1] -= self.rad_to_offset(angle, self.yspeed)[1]
            self.yspeed -= 0.3

        for i in range(5):
            self.rel_points[i][0] += self.rad_to_offset(angle, self.yspeed)[0]
            self.rel_points[i][1] -= self.rad_to_offset(angle, self.yspeed)[1]

        self.centre[0] += self.rad_to_offset(angle, self.yspeed)[0]
        self.centre[1] -= self.rad_to_offset(angle, self.yspeed)[1]

    def move_x(self):
        #ship_img = pygame.image.load('spaceship-on.png')
        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_LEFT]:
            self.xspeed -= 0.01
        elif key[pygame.K_RIGHT]:
            self.xspeed += 0.01

        for i in range(5):
            self.rel_points[i] = list(rotate(self.centre, self.rel_points[i], self.xspeed))

    def edge(self):
        on_screen = 0
        for i in range(5):

            counter = 0
            if self.rel_points[i][0] > screen_size[0]:
                counter += 1
                for i in range(5):
                    self.rel_points[i][0] -= 1
                self.centre[0] -= 1
            if self.rel_points[i][0] < 0:
                counter += 1
                for i in range(5):
                    self.rel_points[i][0] += 1
                self.centre[0] += 1
            if self.rel_points[i][1] > screen_size[1]:
                counter += 1
                for i in range(5):
                    self.rel_points[i][1] -= 1

                self.centre[1] -= 1
            if self.rel_points[i][1] < 0:
                counter += 1
                for i in range(5):
                    self.rel_points[i][1] += 1

                self.centre[1] += 1
            if counter > 0:
                on_screen += 1

        if on_screen > 0:
            self.yspeed = 0-(self.yspeed/2)

    def get_angle(self):
        #rel_points[i] + origin
        from math import atan2, degrees, pi
        dx = self.rel_points[1][0] - self.centre[0]
        dy = self.rel_points[1][1] - self.centre[1]
        rads = atan2(-dy, dx)
        rads %= 2 * pi
        return rads

    def draw(self, surface):
        #print(self.rel_points)
        for i in range(4):

            pygame.draw.line(surface, (255,255,255), self.rel_points[i], self.rel_points[i+1], True)
        pygame.draw.line(surface, (255,255,255), self.rel_points[4], self.rel_points[0], True)

    def update_speed(self):
        if self.xspeed > 0:
            self.xspeed -= 0.005
        if self.yspeed > 0:
            self.yspeed -= 0.1

        if self.xspeed < 0:
            self.xspeed += 0.005
        if self.yspeed < 0:
            self.yspeed += 0.1

        if self.xspeed == 0.02 or self.xspeed == -0.02:
            self.xspeed = 0

        if self.yspeed == 0.005 or self.yspeed == -0.005:
            self.yspeed = 0

        if self.yspeed > 6:
            self.yspeed = 6

        if self.yspeed < -6:
            self.yspeed = -6

        if self.xspeed > 0.1:
            self.xspeed = 0.1

        if self.xspeed < -0.1:
            self.xspeed = -0.1

    def get_pos(self):
        return self.centre

    def Fire(self,screensize):
        self.shot.append(Shot.projectile(self.get_angle(),self.get_pos(),screen_size[0],screen_size[1]))







import copy
import pygame, sys, time
import os
import random
import pygame
import math
import sys
from math import *
import Shot



screen_size = [1300, 600]

shot = []


def main_loop(screen,ship,clock):

    print(len(ship.shot))
    ship.draw(screen)
    ship.move_y()
    ship.move_x()
    ship.update_speed()
    ship.edge()
    key = pygame.key.get_pressed()


    if key[pygame.K_SPACE]:
        if len(ship.shot)<5:
            ship.Fire(screen_size)
            print(ship.shot)
            print("HI")


    for i in range(len(ship.shot)):
        try:
            ship.shot[i].draw(screen)
            ship.shot[i].move()
        except:
            pass
    for i in range(len(ship.shot)-1):
        try:
            if ship.shot[i].killcheck(screen) == True:
                del ship.shot[i]
        except:
            pass


    clock.tick(40)

def main_setup(x,y):
    pygame.init()
    clock = pygame.time.Clock()
    ship = Ship(x,y)
    return clock,ship

def main(screen,clock,ship):
    main_loop(screen,ship,clock)