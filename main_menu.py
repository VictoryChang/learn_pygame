import sys

from pygame.locals import *
import pygame

from game.constants import Color
from game.utility import draw_text


class Project:
    def __init__(self, name: str, screen_width: int, screen_height: int):
        self.name = name
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.main_clock = pygame.time.Clock()

        pygame.init()
        pygame.display.set_caption(self.name)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

    def play(self):

        click = False

        while True:
            self.screen.fill(Color.black)

            background_image = pygame.image.load('/Users/victorychang/Desktop/bg.jpg')
            self.screen.blit(background_image, (0, 0))

            draw_text(self.name, Color.white, self.screen, 50, 60)

            mouse_x, mouse_y = pygame.mouse.get_pos()

            game_button = pygame.Rect(50, 100, 200, 50)
            option_button = pygame.Rect(50, 160, 200, 50)

            if game_button.collidepoint((mouse_x, mouse_y)):
                if click:
                    self.game()

            if option_button.collidepoint((mouse_x, mouse_y)):
                if click:
                    self.options()

            pygame.draw.rect(self.screen, Color.red, game_button)
            pygame.draw.rect(self.screen, Color.red, option_button)

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
            self.main_clock.tick(60)

    def game(self):
        running = True
        while running:
            self.screen.fill(Color.black)

            draw_text('game', Color.white, self.screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            self.main_clock.tick(60)


    def options(self):
        running = True
        while running:
            self.screen.fill(Color.black)

            draw_text('options', Color.white, self.screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            self.main_clock.tick(60)


project = Project(name='Sky', screen_width=500, screen_height=500)
project.play()