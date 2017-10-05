import random
import pygame
import Ship_File




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

def main_setup(screenWidth,screenheight):
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


