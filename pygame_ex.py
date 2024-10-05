import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
x,y=400,300


Car = pygame.image.load("Car.png")
CarRight = pygame.image.load("CarRight.png")
CarLeft = pygame.image.load("CarLeft.png")
CarDown = pygame.image.load("CarDown.png")


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
    if keys[pygame.K_UP]:
        y-=5
        car_image = Car        #will change the image based on users input
    if keys[pygame.K_DOWN]:
        y+=5
        car_image = CarDown

    if keys[pygame.K_LEFT]:
        x-=5
        car_image = CarLeft

    if keys[pygame.K_RIGHT]:
        x+=5
        car_image = CarRight

    screen.blit(car_image, (x, y))        #Adds the image of the car 






    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
