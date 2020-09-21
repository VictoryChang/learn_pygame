import sys

from pygame.locals import *
import pygame

from game.constants import Color
from game.utility import draw_text

main_clock = pygame.time.Clock()



screen_width = 500
screen_height = 500

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)


click = False


def main_menu():
    while True:
        screen.fill(Color.black)
        draw_text('main menu', Color.white, screen, screen_width / 2.0, screen_height / 2.0)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        game_button = pygame.Rect(50, 100, 200, 50)
        option_button = pygame.Rect(50, 200, 200, 50)

        if game_button.collidepoint((mouse_x, mouse_y)):
            if click:
                game()

        if option_button.collidepoint((mouse_x, mouse_y)):
            if click:
                options()

        pygame.draw.rect(screen, Color.red, game_button)
        pygame.draw.rect(screen, Color.red, option_button)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        main_clock.tick(60)


def game():
    running = True
    while running:
        screen.fill(Color.black)

        draw_text('game', Color.white, screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        main_clock.tick(60)


def options():
    running = True
    while running:
        screen.fill(Color.black)

        draw_text('options', Color.white, screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        main_clock.tick(60)


main_menu()