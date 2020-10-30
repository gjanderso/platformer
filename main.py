import pygame, sys
from settings import Settings

from objects import Player


def tower_master():

    pygame.init()
    bg = pygame.image.load("images/background.jpg")

    settings = Settings()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.title)

    character = Player(screen, settings)

    # Main Game Loop
    while True:
        clock.tick(settings.fps)
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    character.move_left()
                if event.key == pygame.K_RIGHT:
                    character.move_right()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    character.move_left(False)
                elif event.key == pygame.K_RIGHT:
                    character.move_right(False)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right')
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left stop')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right stop')
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
        character.update()

        screen.fill(settings.screen_color)
        character.blitme()

        pygame.display.flip()


tower_master()

