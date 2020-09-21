import pygame


def draw_text(text, color, surface, x, y):
    font = pygame.font.SysFont(None, 20)
    text_object = font.render(text, 1, color)
    text_rect = text_object.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_object, text_rect)
