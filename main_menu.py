import pygame

from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT

from game.constants import Color
from game.utility import draw_text


def main_menu(screen_width: int = 800, screen_height: int = 600):
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

            screen.fill(Color.black)
            draw_text(text='main menu', color=Color.white, surface=screen, x=20, y=20)
            pygame.display.flip()


main_menu()
