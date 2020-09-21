# python3 -m pip install -U pygame --user
# python3 -m pygame.examples.aliens

import pygame

COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (0, 0, 255)


def main(window_width: int = 500, window_height: int = 500):
    pygame.init()

    screen = pygame.display.set_mode([window_width, window_height])

    # Run until the user asks to quit
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill(COLOR_WHITE)

        # Draw a solid blue circle in the center
        pygame.draw.circle(screen, COLOR_BLUE, (250, 250), 75)

        # Show the content on the screen
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()


main()
