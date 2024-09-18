import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asterable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asterable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroids = AsteroidField()

    Player.containers = (updatable, drawable)
      
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)
        
        for obj in asterable:
            if obj.collides_with(player):
                print("\nGame over!\n")
                print(f"Your score: {score}")
                sys.exit()
        
            for shot in shots:
                if obj.collides_with(shot):
                    shot.kill()
                    obj.split(score)
    
            

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        

        pygame.display.flip()
        
        dt = clock.tick(30) / 1000


if __name__=="__main__":
    main()
