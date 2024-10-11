import pygame


# pygame setup
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
x,y=0,0

carCenter_Standard = 368, 268
carCenter_45 = 368-(32/3)-1, 268-(32/3)-1 #It just works, Trust me 

carCenter = centerX, centerY = carCenter_Standard     #Corrected for Image Size

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

object_Rect = testObject.get_rect()
object_Rect.width = 64
object_Rect.height = 64
object_Rect.center = ((400)/2 - x, (300)/2 - y)

mapBackS = pygame.transform.scale(mapBack , (2000 , 2000))
Backround_Center = (((2000)/2) - x, ((2000)/2)- y)

font = pygame.font.SysFont('Comic Sans MS', 24)
cordReadOut = font.render(str(x) + "," + str(y), False, (0,0,0))

keyBlock_W = False
keyBlock_A = False
keyBlock_S = False
keyBlock_D = False

def getHitCheck(hitBox):
    if car_Rect.colliderect(hitBox):
        if object_Rect.center(1) >= x:
            keyBlock_A = True
        if object_Rect.center(1) <= x:
            keyBlock_D = True 
        if object_Rect.center(2) >= y:
            keyBlock_W = True
        if object_Rect.center(2) <= y:
            keyBlock_S = True
        
        
        

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("skyblue")

    # RENDER YOUR GAME HERE
    keys=pygame.key.get_pressed()

    if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_DOWN] or keys[pygame.K_s]:

        if keys[pygame.K_UP] or keys[pygame.K_w]:

            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if not(car_Rect.colliderect(object_Rect)):
                    y-=3.5355
                    x-=3.5355
                    carCenter = carCenter_45
                    car_image = pygame.transform.rotate(Car , 45)
                else:
                    y-=3.5355
                    x-=3.5355
                    carCenter = carCenter_45
                    car_image = pygame.transform.rotate(Car , 45)
                    screen.blit(car_image, (carCenter)) 
                    object_Rect.center = ((400/2 - x, 300/2 - y))
                    screen.blit(testObject, (object_Rect.center))
                    if (car_Rect.colliderect(object_Rect)):
                        y+=3.5355
                        x+=3.5355
            
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if not(car_Rect.colliderect(object_Rect)):    
                    y-=3.5355
                    x+=3.5355
                    carCenter = carCenter_45
                    car_image = pygame.transform.rotate(Car , -45) #will change the image based on users input, BUT with pygame Rotate Func
                else:
                    y-=3.5355
                    x+=3.5355
                    carCenter = carCenter_45
                    car_image = pygame.transform.rotate(Car , -45)
                    screen.blit(car_image, (carCenter))
                    object_Rect.center = ((400/2 - x, 300/2 - y))
                    screen.blit(testObject, (object_Rect.center))
                    if (car_Rect.colliderect(object_Rect)):
                        y+=3.5355
                        x-=3.5355
            
            else:
                if not(car_Rect.colliderect(object_Rect)):
                    y-=5
                    carCenter = carCenter_Standard
                    car_image = Car #will change the image based on users input
                else:
                    y-=5
                    carCenter = carCenter_Standard
                    car_image = Car
                    screen.blit(car_image, (carCenter))
                    object_Rect.center = ((400/2 - x, 300/2 - y))
                    screen.blit(testObject, (object_Rect.center))
                    if (car_Rect.colliderect(object_Rect)):
                        y+=5

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:

            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if not(car_Rect.colliderect(object_Rect)):    
                    y+=3.5355
                    x-=3.5355
                    carCenter = carCenter_45
                    car_image = pygame.transform.rotate(Car , 135)
                else:
                    y+=3.5355
                    x-=3.5355
                    carCenter = carCenter_45
                    car_image = pygame.transform.rotate(Car , 135)
                    screen.blit(car_image, (carCenter))
                    object_Rect.center = ((400/2 - x, 300/2 - y))
                    screen.blit(testObject, (object_Rect.center))
                    if (car_Rect.colliderect(object_Rect)):
                        y-=3.5355
                        x+=3.5355
            
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if not(car_Rect.colliderect(object_Rect)):    
                    y+=3.5355
                    x+=3.5355
                    carCenter = carCenter_45
                    car_image = pygame.transform.rotate(Car , 225)
                else:
                    y+=3.5355
                    x+=3.5355
                    carCenter = carCenter_45
                    car_image = pygame.transform.rotate(Car , 225)
                    screen.blit(car_image, (carCenter))
                    object_Rect.center = ((400/2 - x, 300/2 - y))
                    screen.blit(testObject, (object_Rect.center))
                    if (car_Rect.colliderect(object_Rect)):
                        y-=3.5355
                        x-=3.5355

            else:
                if not(car_Rect.colliderect(object_Rect)):    
                    y+=5
                    carCenter = carCenter_Standard
                    car_image = pygame.transform.rotate(Car , 180)
                else:
                    y+=5
                    carCenter = carCenter_Standard
                    car_image = pygame.transform.rotate(Car , 180)
                    screen.blit(car_image, (carCenter))
                    object_Rect.center = ((400/2 - x, 300/2 - y))
                    screen.blit(testObject, (object_Rect.center))
                    if (car_Rect.colliderect(object_Rect)):
                        y-=5
                    
    else:

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if not(car_Rect.colliderect(object_Rect)):    
                x-=5
                carCenter = carCenter_Standard
                car_image = pygame.transform.rotate(Car , 90)
            else:
                x-=5
                carCenter = carCenter_Standard
                car_image = pygame.transform.rotate(Car , 90)
                screen.blit(car_image, (carCenter))
                object_Rect.center = ((400/2 - x, 300/2 - y))
                screen.blit(testObject, (object_Rect.center))
                if (car_Rect.colliderect(object_Rect)):
                    x+=5
                
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if not(car_Rect.colliderect(object_Rect)):    
                x+=5
                carCenter = carCenter_Standard
                car_image = pygame.transform.rotate(Car , -90)
            else:
                x+=5
                carCenter = carCenter_Standard
                car_image = pygame.transform.rotate(Car , -90)
                screen.blit(car_image, (carCenter))
                object_Rect.center = ((400/2 - x, 300/2 - y))
                screen.blit(testObject, (object_Rect.center)) 
                if (car_Rect.colliderect(object_Rect)):
                    x-=5

    
    cordReadOut = font.render(str(round(x)) + "," + str(round(y)), False, (0,0,0))
    
    Backround_Center = (((2000)/2) - x, ((2000)/2)- y)
    object_Rect.center = ((400)/2 - x, (300)/2 - y) # updates tawhe rects position

    screen.blit(mapBackS, (Backround_Center))
    screen.blit(cordReadOut, (width * 0.8, height * 0.1))
    screen.blit(centeringTestImage, (368, 268))
    screen.blit(car_image, (carCenter)) #Adds the image of the car 
    screen.blit(testObject, (object_Rect.center))


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 60

pygame.quit()
