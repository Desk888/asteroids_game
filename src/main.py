import pygame
import sys
from constants import *
from player import Player
from circleshape import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # Initialisation
    pygame.init
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()
    
    # Game Loop
    while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
              return
        screen.fill("black")
        for item in updateable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()  
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    

# Execution
if __name__ == "__main__":
    main()