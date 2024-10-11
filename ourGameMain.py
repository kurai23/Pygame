import pygame


# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption ("Speed Racer") #added Window mode title
x,y = 0, 0
pygame.mixer.music.load('speed.mp3') #added bgm sound
pygame.mixer.music.play(-1)

carCenter_Standard = 368+x, 268+y   # Takes into accout that the image is 64*64 bits
carCenter_45 = (368-(32/3)-1)+x, (268-(32/3)-1)+y # It just works, Trust me 

carCenter = carCenter_Standard  #Corrected for Image Size

Car = pygame.image.load(".\Images\Car_Main.png")
#CarRight = pygame.image.load(".\Images\CarRight.png")
#CarLeft = pygame.image.load(".\Images\CarLeft.png")
#CarDown = pygame.image.load(".\Images\CarDown.png")



car_image = Car        #Default image will be the car facing up

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #added exit on press "esc"
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
    
    carCenter_Standard = 368+x, 268+y
    carCenter_45 = (368-(32/3)-1)+x, (268-(32/3)-1)+y 

    screen.blit(car_image, (carCenter)) #Adds the image of the car 






    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
