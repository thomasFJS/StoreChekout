import pygame 
import random
import sys

import constants

from Client import Client
from Button import Button
from StoreCheckout import StoreCheckout




class Game(object):
    
    def __init__(self):
        #Create sprite lists
        self.all_sprites_list = pygame.sprite.Group()
        self.client = Client()
        self.all_sprites_list.add(self.client)
        self.number = 1
        self.buttons = []
        gui_font = pygame.font.Font(None,30)
        btnFiveClient = Button('Add 5 Clients',200,40,(100,200),5, self.add_five_clients)
        btnAddHours = Button('Add 1 Hour', 200,40,(1200,700),5, self.add_five_clients )
        self.buttons.append(btnFiveClient)

        for i in range(13):
            storeCheckout = StoreCheckout()

            storeCheckout.rect.x = 0
            storeCheckout.rect.y = (i*60+10)
            
            self.all_sprites_list.add(storeCheckout)

    
    def quit_game(self):
        """Callback method to quit the game."""
        self.done = True

    def add_five_clients(self):
        """Callback method to add 5 new clients."""
        for i in range(5):
            client = Client()
            client.rect.x = random.randint(0,constants.SCREEN_WIDTH)
            client.rect.y = random.randint(0,constants.SCREEN_HEIGHT)
            self.all_sprites_list.add(client)



    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
 
        return False

    def run(self):
        self.all_sprites_list.update()
        


    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill(constants.BLACK)
        self.all_sprites_list.draw(screen)
        for b in self.buttons:
            b.draw(screen)
        pygame.display.flip()
 