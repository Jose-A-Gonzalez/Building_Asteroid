from constants import SCREEN_WIDTH,SCREEN_HEIGHT
import pygame
from logger import log_state
from player import Player


def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
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
        pygame.display.flip()
if __name__ == "__main__":
    main()
