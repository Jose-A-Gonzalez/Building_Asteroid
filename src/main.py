from constants import SCREEN_WIDTH,SCREEN_HEIGHT
import pygame
from logger import log_state


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.fill("black")
    pygame.display.flip()
    while True:
        log_state()
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
              return
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
