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
    thrust = 300.0

    _Position = [64,54]
    _Orientation = 000
    __Rotation_Speed = 0
    __Speed = [0,0]

    shot = []

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
        self.shot.append(projectile(self.get_angle(),self.get_pos(),screen_size[0],screen_size[1]))







import copy
import pygame, sys, time
import os
import random
import pygame
import math
import sys
from math import *




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
                print("WTF")
                del ship.shot[i]
                print("IM DEAD")
        except:
            pass


    clock.tick(40)

def main_setup_ship():
    pygame.init()
    clock = pygame.time.Clock()
    ship = Ship([100, 100])
    return clock,ship

def main(screen,clock,ship):
    main_loop(screen,ship,clock)


import random
import pygame





class Rock(pygame.sprite.Sprite):
    def __init__(self, position, size, speed=0):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(("images/rock-" + str(size) + ".png"))

        self.rect = self.image.get_rect()

        self.rect[0] = position[0]
        self.rect[1] = position[1]

        self.speed = speed

    def update(self):
        self.rect = self.rect.move(self.speed)

    def killcheck(self, screen):
        inflatedScreen = screen.get_rect().inflate((self.rect[2] * 2), (self.rect[3] * 2))
        if not inflatedScreen.contains(self.rect):
            self.kill()

    def isclicked(self,ship):
        for i in range(len(ship.shot)):
            if self.rect.collidepoint(ship.shot[i].get_pos()):
                return True

    def size(self):
        return self.size

    def killship(self,relpoints):
        for point in relpoints:
            if self.rect.collidepoint(point):
                return True

    def coords(self):
        return [self.rect[0], self.rect[1]]

    def rotate(self, Surface, angle):
        self.image = pygame.transform.rotate(Surface, angle)
        self.rect = self.image.get_rect()

    def shot(self):
        return self.rect


def Main_Loop(rockList,score,screen,screenWidth,screenheight,clock,ship):
    # Always maintain total rock number on screen
    rockWeight = 0
    for rock in rockList:
        if rock.size == "big":
            rockWeight += 6
        elif rock.size == "normal":
            rockWeight += 4
        elif rock.size == "small":
            rockWeight += 2
    if rockWeight < 70:
        while rockWeight < 70:
            speed = [(random.uniform(-4, 4)), (random.uniform(-4, 4))]
            while abs(speed[0]) <= 1 or abs(speed[1]) <= 1:
                speed = [(random.uniform(-4, 4)), (random.uniform(-4, 4))]

            # Choose random direction to spawn rock from
            rocksize = random.choice(["big", "normal"])
            screenSide = random.choice(["left", "up", "right", "down"])
            if screenSide == "left":
                newRock = Rock([-150, random.randint(0, screenheight)], rocksize, speed)
            elif screenSide == "up":
                newRock = Rock([random.randint(0, screenWidth), -150], rocksize, speed)
            elif screenSide == "right":
                newRock = Rock([screenWidth, random.randint(0, screenheight)], rocksize, speed)
            elif screenSide == "down":
                newRock = Rock([random.randint(0, screenWidth), screenheight], rocksize, speed)

            rockList.add(newRock)

            # Calculate total weight of rocks on screen
            rockWeight = 0
            for rock in rockList:
                if rock.size == "big":
                    rockWeight += 6
                elif rock.size == "normal":
                    rockWeight += 5
                elif rock.size == "small":
                    rockWeight += 2

    # destroy all rocks off screen
    for rock in rockList:
        rock.killcheck(screen)
        if rock.killship(ship.rel_points):
            alive = False
        else:
            alive = True

    # #Rock collision with ship
    # for rock in rockList:
    #     if missile.rect().contains(rock.rect):
    #         DESTROY

    # Rock collision with bullets
    for rock in rockList:
        if rock.isclicked(ship):
            if rock.size == "big":
                currentRockPos = rock.coords()
                rockList.remove(rock)
                score += 10
                for i in range(2):
                    speed = [(random.uniform(-5, 5)), (random.uniform(-5, 5))]
                    newRock = Rock([currentRockPos[0], currentRockPos[1]], "normal",
                                   speed)
                    rockList.add(newRock)
            elif rock.size == "normal":
                currentRockPos = rock.coords()
                rockList.remove(rock)
                score += 5
                for i in range(2):
                    speed = [(random.uniform(-5, 5)), (random.uniform(-5, 5))]
                    newRock = Rock([currentRockPos[0], currentRockPos[1]], "small",
                                   speed)
                    rockList.add(newRock)
            elif rock.size == "small":
                score += 2
                rockList.remove(rock)

    # display update and draw functions
    #clock.tick(60)

    #print(score)

    rockList.update()
    rockList.draw(screen)
    pygame.display.flip()

def newGame(screenWidth,screenheight,screen,rockList,score,clock,ship):

        Main_Loop(rockList, score, screen, screenWidth, screenheight, clock,ship)

def main_setup_ast(screenWidth,screenheight):
    # Set up screen for game

    # screen = pygame.display.set_mode((screenWidth, screenheight))

    score = 0

    # Set up clock to maintain FPS
    clock = pygame.time.Clock()

    # create some rocks
    rockList = pygame.sprite.Group()
    for i in range(5):
        speed = [(random.uniform(-5, 5)), (random.uniform(-5, 5))]
        newRock = Rock([random.randint(0, screenWidth), random.randint(0, screenheight)], "big", speed)
        rockList.add(newRock)

    return rockList,score,clock

from math import *
import copy
import os
def rad_to_offset(radians, offset):  # insert better func name.
    x = cos(radians) * offset
    y = sin(radians) * offset
    return [x, y]

import pygame
class projectile:
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
import os
import pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"



screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("ASTEROIDS")

clock = pygame.time.Clock()

def endscreen(screen):
    gameRunning = False

def main_run():
    screenWidth, screenheight = screen_size[0],screen_size[1]
    gameRunning = True

    clock,ship = main_setup_ship()
    rockList, score, clock = main_setup_ast(screenWidth, screenheight)
    alive = True

    while gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False
        screen.fill((0, 0, 0))
        main_loop(screen,ship,clock)
        newGame(screenWidth,screenheight,screen,rockList,score,clock,ship)
        while alive == False:
            endscreen(screen)

main_run()