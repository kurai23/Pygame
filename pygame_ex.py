import pygame


# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
x,y=400,300


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

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("skyblue")

    # RENDER YOUR GAME HERE
    keys=pygame.key.get_pressed()

    if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_DOWN] or keys[pygame.K_s]:

        if keys[pygame.K_UP] or keys[pygame.K_w]:

            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                y-=3.5355
                x-=3.5355
                car_image = pygame.transform.rotate(Car , 45)
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                y-=3.5355
                x+=3.5355
                car_image = pygame.transform.rotate(Car , -45) #will change the image based on users input, BUT with pygame Rotate Func
            else:
                y-=5
                car_image = Car #will change the image based on users input

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:

            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                y+=3.5355
                x-=3.5355
                car_image = pygame.transform.rotate(Car , 135)
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                y+=3.5355
                x+=3.5355
                car_image = pygame.transform.rotate(Car , 225)
            else:
                y+=5
                car_image = pygame.transform.rotate(Car , 180)
    else:

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x-=5
            car_image = pygame.transform.rotate(Car , 90)

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x+=5
            car_image = pygame.transform.rotate(Car , -90)

    screen.blit(car_image, (x, y)) #Adds the image of the car 






    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
