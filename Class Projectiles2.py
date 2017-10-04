import pygame, time, math, os
from msvcrt import getch
pygame.init()
class Projectiles:

        def get_x_speed_of_projectile(shooting_angle, projectile_speed):
            x_speed_of_projectile = (projectile_speed/90) * shooting_angle
            return x_speed_of_projectile
            #Uses sine rule

        def get_y_speed_of_projectile(projectile_speed, shooting_angle):
            third_angle = 90 - shooting_angle
            y_speed_of_projectile = (projectile_speed/90) * third_angle
            return y_speed_of_projectile

        def shooting_angle_finder(ship_angle):
            shooting_angle = ship_angle
            if shooting_angle >= 90:
                shooting_angle = shooting_angle - 90
            else:
                return shooting_angle

        def shoot(ship_angle, projectile_speed, ship_x_position, ship_y_position):
            shooting_angle = shooting_angle_finder(ship_angle)
            if shooting_angle != 0 or 90 or 180 or 270:
                x_speed_of_projectile = get_x_speed_of_projectile(shooting_angle, projectile_speed)
                y_speed_of_projectile = get_y_speed_of_projectile(projectile_speed, shooting_angle)
            else:
                if shooting_angle == 0:
                    x_speed_of_projectile = 0
                    y_speed_of_projectile = 5
                elif shooting_angle == 90:
                    x_speed_of_projectile = 5
                    y_speed_of_projectile = 0
                elif shooting_angle == 180:
                    x_speed_of_projectile = 0
                    y_speed_of_projectile = -5
                elif shooting_angle == 270:
                    x_speed_of_projectile = -5
                    y_speed_of_projectile = 0

            return [x_speed_of_projectile, y_speed_of_projectile]

                    # animate the projectiles moving.
        #if #collision:
            #do something here
            #time.sleep(firing_rate)
        #else:
            #time.sleep(firing_rate)

firing_rate = 0.5
projectile_speed = 5
ship_x_position = 50
ship_y_position = 50
ship_angle = 45
screen = pygame.display.set_mode((800,800))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    pygame.display.flip()

    # os.chdir("C:\Users\N00191\Downloads")
#    bullet = pygame.image.load("C:\\Users\\N00191\\Downloads\\pictureofbullet.bmp").convert()
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255,255,255), (ship_x_position, ship_y_position), 40)
    fpsClock = pygame.time.Clock()
#    imageX = 200
#    bulletY = 200
    running = True

    #screen.blit(bullet,(ship_x_position, ship_y_position))

    key = ord(getch())
    if key == 1:
        projectile_movement = shoot(ship_angle, projectile_speed, ship_x_position, ship_y_position)
        print(projectile_movement)
    else:
        one = 1

    ship_x_position = ship_x_position + 1