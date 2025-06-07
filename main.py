import pygame
from constants import *
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT), flags=0, depth=0, display=0, vsync=0)
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           return
if __name__ == "__main__":
    main()
