import pygame

from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT


class Color:
    black = (0, 0, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill(Color.white)
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)  # move in place
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


def create_game(screen_width: int, screen_height: int):
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    player = Player()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.type == QUIT:
                    running = False

            pressed_keys = pygame.key.get_pressed()
            player.update(pressed_keys)

            screen.fill(Color.black)
            screen.blit(player.surf, player.rect)
            pygame.display.flip()


create_game(screen_width=800, screen_height=600)
