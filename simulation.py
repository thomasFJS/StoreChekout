import pygame 
import random
import sys
from Button import Button
from Client import Client
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
CLIENT_SIZE = 25
STORECHEKOUT_SIZE = 50
 



class StoreCheckout(pygame.sprite.Sprite):
    """
    Class to keep track of a storecheckout's status {1 => Open | 0 => Closed}
    """
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.width = STORECHEKOUT_SIZE
        self.height = STORECHEKOUT_SIZE
        self.color = GREEN
        self.status = 0

    def draw(self, screen):
        """
        Function to draw storecheckout.
        """
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        
##class Client(pygame.sprite.Sprite):
##    """
##    Class to keep track of a client's location and vector.
##    """
##    def __init__(self):
##        super().__init__()
##        self.x = random.randrange(CLIENT_SIZE, SCREEN_WIDTH - CLIENT_SIZE)
##        self.y = random.randrange(CLIENT_SIZE, SCREEN_HEIGHT - CLIENT_SIZE)
##        self.size = 25
##        self.color = WHITE
##        self.change_x = random.randrange(-2, 3)
##        self.change_y = random.randrange(-2, 3)
##
##    def draw(self, screen):
##        """
##        Function to draw client.
##        """
##        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)


def generate_new_client():
    """
    Function to make a new, random client.
    """
    newclient = Client(WHITE, CLIENT_SIZE,CLIENT_SIZE)
    # Starting position of the client.
    # Take into account the client size so we don't spawn on the edge.
    newclient.x = random.randrange(CLIENT_SIZE, SCREEN_WIDTH - CLIENT_SIZE)
    newclient.y = random.randrange(CLIENT_SIZE, SCREEN_HEIGHT - CLIENT_SIZE)
 
    # Speed and direction of rectangle
    newclient.change_x = random.randrange(-2, 3)
    newclient.change_y = random.randrange(-2, 3)
 
    return newclient

def make_clients(number):
    clients_list = []
    for i in range(number):
        client = generate_new_client()
        clients_list.append(client)


    return clients_list

def make_storecheckout(number):
    storecheckout_list = []
    for x in range(number):
        storeCheckout = StoreCheckout()
        storeCheckout.y = (x*60+10)
        storecheckout_list.append(storeCheckout)
    return storecheckout_list

def add_one_hour():
    print ("oui")


class Simulation:

    def __init__(self, screen):
        self.done = False
        self.clock = pygame.time.Clock()
        self.screen = screen
        # Contains all sprites. Also put the button sprites into a
        # separate group in your own game.
        self.buttons_sprites = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
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
        
        storecheckout_list = make_storecheckout(13)
        clients_list = make_clients(10)
        for c in clients_list:
            self.all_sprites.add(c)

        for s in storecheckout_list:
            self.all_sprites.add(s)
        # Add the button sprites to the sprite group.
        self.buttons_sprites.add(self.start_button, self.quit_button)

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            for button in self.buttons_sprites:
                button.handle_event(event)

    def run_logic(self):
        self.all_sprites.update(self.dt)

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

def main():
    """
    This is our main program.
    """
    pygame.init()
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Store")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    gui_font = pygame.font.Font(None,30)
    buttons = []
    button1 = Button('+1 Hour',150,40,(1250,700),5, gui_font)
    button2 = Button('+5 Clients',150,40,(1250,650),5, gui_font)
    buttons.append(button1)
    buttons.append(button2)



    storecheckout_list = make_storecheckout(13)

    clients_list = make_clients(10)
 
    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # Space bar! Spawn a new client.
                if event.key == pygame.K_SPACE:
                    client = make_client()
                    client_list.append(client)
 
        # --- Logic
        for client in client_list:
            # Move the client's center
            client.x += client.change_x
            client.y += client.change_y
 
            # Bounce the client if needed
            if client.y > SCREEN_HEIGHT - CLIENT_SIZE or client.y < CLIENT_SIZE:
                client.change_y *= -1
            if client.x > SCREEN_WIDTH - CLIENT_SIZE or client.x < STORECHEKOUT_SIZE:
                client.change_x *= -1
 
        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)
 
        # Draw the clients
        for client in clients_list:
            client.draw(screen)

        # Draw the storechekout
        for storeCheckout in storecheckout_list:
            storeCheckout.draw(screen)

        for b in buttons:
            b.draw(screen)
        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()



if __name__ == '__main__':
    pygame.init()
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    FONT = pygame.font.SysFont('Comic Sans MS', 32)
    # Default button images/pygame.Surfaces.
    IMAGE_NORMAL = pygame.Surface((100, 32))
    IMAGE_NORMAL.fill(pygame.Color('dodgerblue1'))
    IMAGE_HOVER = pygame.Surface((100, 32))
    IMAGE_HOVER.fill(pygame.Color('lightskyblue'))
    IMAGE_DOWN = pygame.Surface((100, 32))
    IMAGE_DOWN.fill(pygame.Color('aquamarine1')) 
    pygame.display.set_caption("Store")
    Simulation(screen).run()
    pygame.quit()