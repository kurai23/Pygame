import sys
import pygame as pg
import math
import time
pg.init()

running = True
size = width, height = (1080, 720)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()

carx, cary = 540, 360
car = carcenter, cardirection = (carx, cary), math.radians(-90)
carsquare = (carx,cary),(380,240),(0, 0)
momentum = 0

pg.display.init()
while running == True:
   
    #kills program on top right X click
    deltatime = clock.tick(60) / 1000
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
   
    #draws the screen
    screen.fill("skyblue")
    pg.draw.polygon(screen, "red", carsquare)
    pg.display.flip()
   
    #keypress code
    keys = pg.key.get_pressed()

    #turning
    if keys[pg.K_a] and abs(momentum) > 1:
        cardirection -= math.radians(60) * deltatime
    
    if keys[pg.K_d] and abs(momentum) > 1:
        cardirection += math.radians(60) * deltatime
    
    #Acceleration (gas and brakes)
    if keys[pg.K_w]:
        momentum += 13 
    
    if keys[pg.K_s]:
        momentum -= 8 
    
    if keys[pg.K_SPACE]:
        if abs(momentum) < 1:
            momentum = 0
        else:
            momentum *= 0.94
    
    #car position code
    carx += momentum * math.cos(cardirection) * deltatime
    cary += momentum * math.sin(cardirection) * deltatime
    
    carsize = 30

    # def draw_car():
    #     leftx = carsize * math.cos(cardirection - math.radians(30)) 
    #     lefty = carsize * math.sin(cardirection - math.radians(30)) 
    #     rightx = carsize * math.cos(cardirection + math.radians(30)) 
    #     righty = carsize * math.sin(cardirection + math.radians(30))
    
    leftx = carsize * math.cos(cardirection - math.radians(30)) 
    lefty = carsize * math.sin(cardirection - math.radians(30)) 
    rightx = carsize * math.cos(cardirection + math.radians(30)) 
    righty = carsize * math.sin(cardirection + math.radians(30)) 
    
    carsquare = (leftx + carx, lefty + cary), (rightx + carx, righty + cary), (carx - leftx, cary - lefty) , (carx - rightx, cary - righty)

pg.quit()
