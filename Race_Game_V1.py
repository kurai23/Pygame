import pygame
import math


# pygame setup
pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True

x,y,r = 0,0,360
a = 0
a_X, a_Y = 0,0

# a = 0.7677650582



def limit(Varible, minV, maxV):
    return max(min(maxV, Varible), minV)

# Another Don't worry about it
def findCarCenter():
    return ((width-64)/2)-((12)*limit(((math.sin((r*0.06981317)+((3*math.pi)/2)))+1)*(0.7677650582), 0, 1)), ((height-64)/2)-((12)*limit(((math.sin((r*0.06981317)+((3*math.pi)/2)))+1)*(0.7677650582), 0, 1))

#carCenter_Standard = (width-64)/2, ((height-64)/2)
#carCenter_45 = 368-(32/3)-1, 268-(32/3)-1 #It just works, Trust me \
carCenter_R = findCarCenter()

carCenter = centerX, centerY = carCenter_R   #Corrected for Image Size

Car = pygame.image.load(".\Images\Car_Main.png")
centeringTestImage = pygame.image.load(".\Images\centeringTestImage.png")
testObject = pygame.image.load(".\Images\_testObject.png")
#testBackround = pygame.image.load(".\Images\_testLARGE.png")
mapBack = pygame.image.load(".\Images\RaceTrack_500x500.png")

car_image = Car     #Default image will be the car facing up
car_Rect = Car.get_rect()
car_Rect.width = 64
car_Rect.height = 64
car_Rect.center = (carCenter)

def findObjectCenter():
    object_Rect.center = (((400-64)/2) + 128 - x, ((300-64)/2) + 64 - y)

object_Rect = testObject.get_rect()
object_Rect.width = 64-5
object_Rect.height = 64-5
findObjectCenter()

mapBackS = pygame.transform.scale_by(mapBack , (10))
Backround_Center = (((400-5000)/2) - x, ((300-5000)/2)- y)

font = pygame.font.SysFont('Comic Sans MS', 24)
cordReadOut = font.render(str(x) + "," + str(y), False, (0,0,0))

#keyBlock_W = False
#keyBlock_A = False
#keyBlock_S = False
#keyBlock_D = False

""""
def getHitCheck(X, p1, Y, p2,   ):
    y p1= Y
    x p2= X
    carCenter = carCenter_45
    car_image = pygame.transform.rotate(Car , 45)
    screen.blit(car_image, (carCenter)) 
    object_Rect.center = ((400/2 - x, 300/2 - y))
    screen.blit(testObject, (object_Rect.center))
    if (car_Rect.colliderect(object_Rect)):
        y+=3.5355
        x+=3.5355

"""
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys=pygame.key.get_pressed()

    
    # Adds Turning
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        r += 0.5*(a/3.5)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        r -= 0.5*(a/3.5)

    if r > 360: 
        r = 0
    if r < 0:
        r = 360
    
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        a += 0.1
    elif keys[pygame.K_SPACE]:
        if a > 0:
            a -= 0.1
        if a < 0:
            a += 0.1
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        a -= 0.1

    # Slows Down Car
    if a > 0:
        a -= 0.05
    if a < 0:
        a += 0.05

    a = limit(a, -8, 8)
    """
    a_X += math.sin(math.radians(r))*a
    a_X = limit(a_X, -math.sin(math.radians(r))*a, math.sin(math.radians(r))*a)
    a_Y += math.cos(math.radians(r))*a
    a_Y = limit(a_Y, -math.cos(math.radians(r))*a, math.cos(math.radians(r))*a)
    """
    x -= math.sin(math.radians(r))*a
    y -= math.cos(math.radians(r))*a




    car_image = pygame.transform.rotate(Car , r)
    carCenter_R = findCarCenter()
    carCenter = carCenter_R
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("skyblue")

    # RENDER YOUR GAME HERE

    cordReadOut = font.render(str(round(x)) + "," + str(round(y)) + "," + str(round(r)), False, (0,0,0))
    testWrite = font.render(str(a), False, (0,0,0))

    Backround_Center = (((400-5000)/2) - x, ((300-5000)/2)- y)
    findObjectCenter() # updates the rects position

    screen.blit(mapBackS, (Backround_Center))
    screen.blit(testWrite, (width * 0.8, height * 0.15))
    screen.blit(cordReadOut, (width * 0.8, height * 0.1))
    screen.blit(car_image, (carCenter)) #Adds the image of the car 
    screen.blit(testObject, (object_Rect.center))
    #screen.blit(centeringTestImage, (368, 268))


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 60

pygame.quit()
