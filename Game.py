import pygame 
import random
import sys
import numpy

import constants

from Client import Client
from Button import Button
from StoreCheckout import StoreCheckout




class Game(object):
    
    def __init__(self):
        #Create sprite lists
        self.all_sprites_list = pygame.sprite.Group()
        self.clients_sprites_list = pygame.sprite.Group()
        #self.client = Client()
        #self.clients_sprites_list.add(self.client)
        #self.all_sprites_list.add(self.client)
        self.number = 1

        self.index = numpy.argmax(numpy.array(constants.NB_CLIENT_BY_HOUR) > 0) #Index of the first value in array which is greater than 0
        
        self.buttons = []
        gui_font = pygame.font.Font(None,30)
        btnFiveClient = Button('Add 5 Clients',200,40,(990,660),5, self.add_five_clients)
        btnAddHours = Button('Add 1 Hour', 200,40,(1200,660),5, self.add_five_clients )
        btnStart = Button('Start', 410,40,(990,710),5, self.start)
        self.buttons.append(btnFiveClient)
        self.buttons.append(btnAddHours)
        self.buttons.append(btnStart)
        self.hour_pass_event = pygame.USEREVENT+1
        pygame.time.set_timer(self.hour_pass_event, 60000)

        for i in range(13):
            storeCheckout = StoreCheckout()

            storeCheckout.rect.x = 0
            storeCheckout.rect.y = (i*60+10)
            
            self.all_sprites_list.add(storeCheckout)

    
    def quit_game(self):
        """Callback method to quit the game."""
        self.done = True

    def add_clients(self, number):

        for i in range(number):
            client = Client()
            client.rect.x = random.randint(0,constants.SCREEN_WIDTH)
            client.rect.y = random.randint(0,constants.SCREEN_HEIGHT)
            self.all_sprites_list.add(client)
            self.clients_sprites_list.add(client)

    def add_five_clients(self):
        """Callback method to add 5 new clients."""
        self.add_clients(5)

    def start(self):
        self.add_clients(constants.NB_CLIENT_BY_HOUR[self.index])


    

    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """
 
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                for c in self.clients_sprites_list:
                    if c.counter <= 0:
                        c.color = constants.RED
                    else:    
                        c.counter-=1
                    print(c.counter)
            if event.type == self.hour_pass_event:
                self.index +=1
                self.add_clients(constants.NB_CLIENT_BY_HOUR[self.index])
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
 