from constants import SCREEN_WIDTH,SCREEN_HEIGHT
import pygame
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots,drawable,updatable)
    AsteroidField.containers = (updatable) 
    Asteroid.containers = (updatable,drawable,asteroids)
    Player.containers = (updatable, drawable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    while True:
        log_state()
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
              return
        dt = clock.tick(60)/1000
        screen.fill("black")
        for dra in drawable:
            dra.draw(screen)
        updatable.update(dt)
        for aste in asteroids:
            for dr in drawable:
                if aste.collide_with(dr) and dr not in asteroids and dr not in shots:
                    log_event("player_hit")
                    print("Game Over!")
                    sys.exit()
            for shot in shots:
                if aste.collide_with(shot):
                    log_event("asteroid_shot")
                    aste.split()
                    shot.kill()
        pygame.display.flip()
if __name__ == "__main__":
    main()
