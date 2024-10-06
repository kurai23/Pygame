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
#CarRight = pygame.image.load(".\Images\CarRight.png")
#CarLeft = pygame.image.load(".\Images\CarLeft.png")
#CarDown = pygame.image.load(".\Images\CarDown.png")


car_image = Car     #Default image will be the car facing up

font = pygame.font.SysFont('Comic Sans MS', 24)
cordReadOut = font.render(str(x) + "," + str(y), False, (0,0,0))

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
                y-=3.5355
                x-=3.5355
                carCenter = carCenter_45
                car_image = pygame.transform.rotate(Car , 45)
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                y-=3.5355
                x+=3.5355
                carCenter = carCenter_45
                car_image = pygame.transform.rotate(Car , -45) #will change the image based on users input, BUT with pygame Rotate Func
            else:
                y-=5
                carCenter = carCenter_Standard
                car_image = Car #will change the image based on users input

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:

            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                y+=3.5355
                x-=3.5355
                carCenter = carCenter_45
                car_image = pygame.transform.rotate(Car , 135)
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                y+=3.5355
                x+=3.5355
                carCenter = carCenter_45
                car_image = pygame.transform.rotate(Car , 225)
            else:
                y+=5
                carCenter = carCenter_Standard
                car_image = pygame.transform.rotate(Car , 180)
    else:

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x-=5
            carCenter = carCenter_Standard
            car_image = pygame.transform.rotate(Car , 90)

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x+=5
            carCenter = carCenter_Standard
            car_image = pygame.transform.rotate(Car , -90)

    cordReadOut = font.render(str(round(x)) + "," + str(round(y)), False, (0,0,0))
    
    screen.blit(cordReadOut, (width * 0.8, height * 0.1))
    screen.blit(centeringTestImage, (368, 268))
    screen.blit(car_image, (carCenter)) #Adds the image of the car 
    screen.blit(testObject, (400/2 - x, 300/2 - y))






    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
