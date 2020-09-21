import pygame

from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT


class Color:
    black = (0, 0, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)

screen_width = 800
screen_height = 600


def draw_text(text, color, surface, x, y):
    font = pygame.font.SysFont(None, 20)
    text_object = font.render(text, 1, color)
    text_rect = text_object.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_object, text_rect)


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
            draw_text(text='main menu', color=Color.white, surface=screen, x=20, y=20)
            pygame.display.flip()


main_menu()
