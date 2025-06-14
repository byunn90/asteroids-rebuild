import pygame
from constants import *
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = clock(60) / 1000
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
       for event in pygame.event.get():
         if event.type == pygame.QUIT:
             return
         screen.fill("black")
         pygame.display.flip()
         dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
