import pygame

from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT


class Color:
    black = (0, 0, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)

screen_width = 800
screen_height = 600


def main_menu():
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
            pygame.display.flip()


main_menu()
