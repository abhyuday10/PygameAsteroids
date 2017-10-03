import pygame, sys, time
import os
import random
import pygame
import math
import sys
from math import *


os.environ["SDL_VIDEO_CENTERED"] = "1"
screen_size = [1300,600]

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("ASTEROIDS")

clock = pygame.time.Clock()

#global ship_img
#ship_img = pygame.image.load('spaceship-on.png')


def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return (qx,qy)



class Ship:
    thrust = 300.0

    _Position = [64,54]
    _Orientation = 000
    __Rotation_Speed = 0
    __Speed = [0,0]

    def __init__(self, position):
        self.position = list(position)
        self.velocity = [0.0, 0.0]

        self.angle = 180.0

        self.fire = 0.0
        self.bullets = []

        # List of (angle,radius) pairs.
        self.rel_points = [[(screen_size[0]/2)-25, (screen_size[1]/2)-25], [(screen_size[0]/2), (screen_size[1]/2)+25], [(screen_size[0]/2)+25, (screen_size[1]/2)-25], [(screen_size[0]/2), (screen_size[1]/2)-10],[(screen_size[0]/2)-25, (screen_size[1]/2)-25]]
        self.centre = [screen_size[0]/2,screen_size[1]/2]
        scale = 0.5
        #for i in range(len(self.rel_points)):
            #self.rel_points[i] = (math.radians(self.rel_points[i][0]), scale * self.rel_points[i][1])

        self.thrust_append = 0

        self.alive = True
        self.dying = False
        self.lives = 3
        self.time_invincibility = 0

        self.score = 0
        self.xspeed = 0
        self.yspeed = 0


    #def __init__(self):
     #   self.rect = pygame.Rect(20,20,0,0)
    def get_collision(self,enemy_pos):
        #Needs Position
        pass

    def shoot_projectile(self):
        bullet = Projectile()
        pass



    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_LEFT]:
           self.rect.move_ip(-1, 0)
        if key[pygame.K_RIGHT]:
           self.rect.move_ip(1, 0)
        if key[pygame.K_UP]:
           self.rect.move_ip(0, -1)
        if key[pygame.K_DOWN]:
           self.rect.move_ip(0, 1)

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
            if self.rel_points[i][0] < 0:
                counter += 1
            if self.rel_points[i][1] > screen_size[1]:
                counter += 1
            if self.rel_points[i][1] < 0:
                counter += 1
            if counter > 0:
                on_screen += 1

        if on_screen > 0:
            self.yspeed = 0-self.yspeed


    def keep_on_screen(self):
        on_screen = 0
        for i in range(5):

            counter = 0
            if self.rel_points[i][0] > screen_size[0]:
                counter += 1
            if self.rel_points[i][0] < 0:
                counter += 1
            if self.rel_points[i][1] > screen_size[1]:
                counter += 1
            if self.rel_points[i][1] < 0:
                counter += 1
            if counter > 0:
                on_screen += 1

            #print (on_screen)

        if on_screen > 0:
            fake_points = [[0,0],[0,0],[0,0],[0,0],[0,0]]
            for i in range(5):
                if self.rel_points[i][0] < 0:
                    fake_points[i][0] = self.rel_points[i][0] % screen_size[0]
            for i in range(5):
                fake_points[i][1] = self.rel_points[i][1] % screen_size[1]


            print(fake_points)

            for i in range(5):
                if self.rel_points[i][0] > screen_size[0] and self.rel_points[i][1] > screen_size[1]:
                    pygame.draw.line(screen, (255,255,255), fake_points[i], (0,0), True)
                if self.rel_points[i][0] > screen_size[0] and self.rel_points[i][1] < 0:
                    pygame.draw.line(screen, (255,255,255), fake_points[i], (0,screen_size[1]), True)

                if self.rel_points[i][1] < 0 and self.rel_points[i][1] > screen_size[1]:
                    pygame.draw.line(screen, (255,255,255), fake_points[i], (screen_size[0],0), True)
                if self.rel_points[i][1] < 0 and self.rel_points[i][1] < 0:
                    pygame.draw.line(screen, (255,255,255), fake_points[i], (screen_size[0],screen_size[1]), True)



            pygame.draw.line(screen, (255,255,255), fake_points[i], fake_points[0], True)

        if on_screen == 5:
            for i in range(5):
                for k in range(1):
                    self.rel_points[i][k] = self.rel_points[i][k]% screen_size[k]


    def get_angle(self):
        #rel_points[i] + origin
        from math import atan2, degrees, pi
        dx = self.rel_points[1][0] - self.centre[0]
        dy = self.rel_points[1][1] - self.centre[1]
        rads = atan2(-dy, dx)
        rads %= 2 * pi
        return rads

    def get_pos(self):
        return self._Position

    def update_pos(self):
        self.rect = (self._Position[0],self._Position[1])

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

        if self.yspeed > 10:
            self.yspeed = 10

        if self.yspeed < -10:
            self.yspeed = -10

        if self.xspeed > 0.3:
            self.xspeed = 0.3

        if self.xspeed < -0.3:
            self.xspeed = -0.3

    def Fire(self):
        shot = Projectile()






class Projectile(Ship):

    def __init__(self):
        angle = ship.get_angle()
        yspeed = ship.yspeed
        rel_points = [[ship.rel_points[1]]]
        pass

    def draw(self,surface):
        offset0 = self.rad_to_offset(ship.get_angle(), ship.yspeed)
        offset1 = self.rad_to_offset(ship.get_angle(), ship.yspeed)
        pygame.draw.line(surface, (255,255,255), self.rel_points[0], [self.rel_points[0][0] + offset0,self.rel_points[0][1] + offset1,], True)

    def move(self):
        self.rel_points[0] += self.rad_to_offset(self.angle, self.yspeed)[0]
        self.centre[1] -= self.rad_to_offset(self.angle, self.yspeed)[1]




ship = Ship([100,100])
ship.shot = ""


pygame.init()

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    ship.draw(screen)
    ship.move_y()
    ship.move_x()
    ship.update_speed()
    ship.edge()
    key = pygame.key.get_pressed()
    dist = 1
    if key[pygame.K_SPACE]:
        ship.Fire()
    try:
        ship.shot.draw()
        ship.shot.move()
    except:
        pass
    #print(ship.centre)
    #ship_img = ship.move_x(ship_img)
    #ship_img = ship.move_x(ship_img)


    #print(ship_img)
    #screen.blit(ship_img,ship.rect)
    pygame.display.update()

    clock.tick(40)
