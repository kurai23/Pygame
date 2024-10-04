# This example was taken straight from the pygame docs, feel free to play around with it.
# The best way to get familiar with a new language/library is to play around with code and
# frequently visit its official documentation: https://www.pygame.org/docs/

# this example will display a purple pygame window. You can draw whatever by using the docs ^

# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
x,y=400,300

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
    if keys[pygame.K_DOWN]:
        y+=5
    if keys[pygame.K_LEFT]:
        x-=5
    if keys[pygame.K_RIGHT]:
        x+=5

        pygame.draw.rect(screen, (255, 0, 0), (x,y,50,50))





    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
