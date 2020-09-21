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

    def update(self, pressed_key, screen_width: int, screen_height: int):
        """
        Move the sprite based on user keypress and keep the player on the screen
        """
        if pressed_key[K_UP]:
            self.rect.move_ip(0, -5)  # move in place
        if pressed_key[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_key[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_key[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height


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

            pressed_key = pygame.key.get_pressed()
            player.update(pressed_key, screen_width, screen_height)

            screen.fill(Color.black)
            screen.blit(player.surf, player.rect)
            pygame.display.flip()


create_game(screen_width=800, screen_height=600)
