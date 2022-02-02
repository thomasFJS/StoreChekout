import pygame
# Import constants file
import constants

from Game import Game
 
def main():
    pygame.init()

    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("StoreChekout")

    done = False
    clock = pygame.time.Clock()

    game = Game()

    while not done:
        done = game.process_events()
        game.run()
        game.display_frame(screen)

        clock.tick(60)
        
    pygame.quit()


if __name__ == "__main__":
    main()