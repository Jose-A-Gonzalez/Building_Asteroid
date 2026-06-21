from constants import SCREEN_WIDTH,SCREEN_HEIGHT
import pygame
from logger import log_state


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.fill("black")
    pygame.display.flip()
    while True:
        # print(f"Starting Asteroids with pygame version {pygame.version.ver}")
        # print(f"Screen width: {SCREEN_WIDTH}")
        # print(f"Screen height: {SCREEN_HEIGHT}")
        log_state()
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
              return

if __name__ == "__main__":
    main()
