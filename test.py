import pygame as pg
from Button import Button
from Client import Client

pg.init()

screen = pg.display.set_mode((800, 600))
FONT = pg.font.SysFont('Comic Sans MS', 32)
# Default button images/pygame.Surfaces.
IMAGE_NORMAL = pg.Surface((100, 32))
IMAGE_NORMAL.fill(pg.Color('dodgerblue1'))
IMAGE_HOVER = pg.Surface((100, 32))
IMAGE_HOVER.fill(pg.Color('lightskyblue'))
IMAGE_DOWN = pg.Surface((100, 32))
IMAGE_DOWN.fill(pg.Color('aquamarine1'))

class Game:

    def __init__(self, screen):
        self.done = False
        self.clock = pg.time.Clock()
        self.screen = screen
        # Contains all sprites. Also put the button sprites into a
        # separate group in your own game.
        self.all_sprites = pg.sprite.Group()
        self.number = 0
        # Create the button instances. You can pass your own images here.
        self.start_button = Button(
            320, 70, 170, 65, self.increment_number,
            FONT, 'Increment', (255, 255, 255),
            IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # If you don't pass images, the default images will be used.
        self.quit_button = Button(
            320, 240, 170, 65, self.quit_game,
            FONT, 'Quit', (255, 255, 255))

        for i in range(number):
            client = generate_new_client()()
            clients_list.append(client)
        # Add the button sprites to the sprite group.
        self.all_sprites.add(self.start_button, self.quit_button)

    def quit_game(self):
        """Callback method to quit the game."""
        self.done = True

    def increment_number(self):
        """Callback method to increment the number."""
        self.number += 1
        print(self.number)

    def run(self):
        while not self.done:
            self.dt = self.clock.tick(30) / 1000
            self.handle_events()
            self.run_logic()
            self.draw()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            for button in self.all_sprites:
                button.handle_event(event)

    def run_logic(self):
        self.all_sprites.update(self.dt)

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.all_sprites.draw(self.screen)
        pg.display.flip()


if __name__ == '__main__':
    pg.init()
    Game(screen).run()
    pg.quit()