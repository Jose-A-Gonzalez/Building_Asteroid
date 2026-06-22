from constants import SCREEN_WIDTH,SCREEN_HEIGHT
import pygame
from logger import log_state
from player import Player


def main():
    pygame.init()
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
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
if __name__ == "__main__":
    main()
