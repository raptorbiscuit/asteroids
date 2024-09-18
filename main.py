import pygame
# https://www.pygame.org/docs/ref/pygame.html
from constants import *

def main():
    pygame.init()
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    whileX = True
    while(whileX):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip()


if __name__=="__main__":
    main()
