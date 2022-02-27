import pygame 
import random
import sys
import numpy

import constants

from Client import Client
from Button import Button
from StoreCheckout import StoreCheckout
from Infos import Infos




class Game(object):
    
    def __init__(self):
        #Create sprite lists
        self.all_sprites_list = pygame.sprite.Group()
        self.clients_sprites_list = pygame.sprite.Group()
        self.checkout_sprites_list = pygame.sprite.Group()
        #self.client = Client()
        #self.clients_sprites_list.add(self.client)
        #self.all_sprites_list.add(self.client)
        self.number = 1
        self.infos = Infos(self.checkout_sprites_list, self.clients_sprites_list)
        self.all_sprites_list.add(self.infos)
        self.index = numpy.argmax(numpy.array(constants.NB_CLIENT_BY_HOUR) > 0) #Index of the first value in array which is greater than 0 (Represent Hours)
        
        self.minutesElapsed = 0

        #BUTTONS
        self.buttons = []
        gui_font = pygame.font.Font(None,30)
        btnFiveClient = Button('Add 5 Clients',200,40,(990,660),5, self.add_five_clients)
        btnAddHours = Button('Add 1 Hour', 200,40,(1200,660),5, self.add_hours )
        btnStart = Button('Start', 410,40,(990,710),5, self.start)
        btnParam = Button('Param', 410,40,(990,760),5, self.open_param)
        self.buttons.append(btnFiveClient)
        self.buttons.append(btnAddHours)
        self.buttons.append(btnStart)
        self.buttons.append(btnParam)

        #EVENTS
        self.hour_pass_event = pygame.USEREVENT+1
        self.go_checkout_event = pygame.USEREVENT+2
        self.time_elapsed_event = pygame.USEREVENT+3
        

        for i in range(13):
            storeCheckout = StoreCheckout()

            storeCheckout.rect.x = 0
            storeCheckout.rect.y = (i*60+10)
            
            self.checkout_sprites_list.add(storeCheckout)
            self.all_sprites_list.add(storeCheckout)

    
    def quit_game(self):
        """Callback method to quit the game."""
        self.done = True

    def open_param(self):
        """Callback method to open param form"""
        exec(open('param.py').read())

    def add_clients(self, number):
        #Clients add function
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
        """Callback method to start the simulation."""
        pygame.time.set_timer(self.hour_pass_event, 60000)
        pygame.time.set_timer(self.time_elapsed_event, 1000)
        self.add_clients(constants.NB_CLIENT_BY_HOUR[self.index])

    def add_hours(self):
        """Callback method to add 1 hour to the simulation."""
        self.index += 1
        self.add_clients(constants.NB_CLIENT_BY_HOUR[self.index])


    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                for c in self.clients_sprites_list:
                    if c.counter <= 0 or c.shoppingFinished == True:
                        c.color = constants.RED
                        c.shoppingFinished = True
                        c.counter+=1
                        pygame.time.set_timer(self.go_checkout_event, 100)
                        #c.goCheckout(self.checkout_sprites_list)
                    else:    
                        c.counter-=1
                        c.color = pygame.Color(c.counter*2,c.counter*2,c.counter*2)

                for checkout in self.checkout_sprites_list:
                    for client in checkout.clientWaiting:
                        if client.checkingOut == True :
                            client.timeToCheckout-=1
                            if client.timeToCheckout <= 0:
                                checkout.clientWaiting.remove(client)
                                self.clients_sprites_list.remove(client)
                                self.all_sprites_list.remove(client)
                   # print(c.counter)
            if event.type == self.go_checkout_event:
                for c in self.clients_sprites_list:
                    if c.shoppingFinished == True and c.checkingOut == False :
                        c.goCheckout(self.checkout_sprites_list)
            if event.type == self.time_elapsed_event:
                self.minutesElapsed += 1
                if self.minutesElapsed <= 9:
                    self.infos.updateValues(self.checkout_sprites_list, self.clients_sprites_list, str(self.index) + ": 0" + str(self.minutesElapsed))
                else:
                    self.infos.updateValues(self.checkout_sprites_list, self.clients_sprites_list, str(self.index) + ": " + str(self.minutesElapsed))
            if event.type == self.hour_pass_event:
                self.minutesElapsed = 0
                self.index +=1
                self.add_clients(constants.NB_CLIENT_BY_HOUR[self.index])
            if event.type == pygame.QUIT:
                return True
 
        return False

    def run(self):
        self.all_sprites_list.update()
        


    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill(constants.WHITE)
        self.all_sprites_list.draw(screen)
        for b in self.buttons:
            b.draw(screen)
        pygame.display.flip()
 