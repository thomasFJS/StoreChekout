import pygame

import constants

from random import randint
 
class Client(pygame.sprite.Sprite):
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.color = constants.WHITE

        self.shoppingFinished = False
        self.checkingOut = False

        self.image = pygame.Surface([constants.CLIENT_SIZE, constants.CLIENT_SIZE])
        self.image.fill(self.color)
 
        self.counter = randint(randint(constants.MIN_TIME_IN_STORE_FROM,constants.MIN_TIME_IN_STORE_TO),randint(constants.MAX_TIME_IN_STORE_FROM,constants.MAX_TIME_IN_STORE_TO))
        self.timeToCheckout = round(self.counter/5)
        
        
        self.text = str(self.counter).rjust(3)
        self.textsurface = pygame.font.Font(None,30).render(self.text, True, constants.BLACK)
        self.textrect = self.textsurface.get_rect(center=self.image.get_rect().center)
        
        #pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.velocity = [randint(4,8),randint(-8,8)]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.rect.x >= constants.SCREEN_WIDTH-constants.CLIENT_SIZE or self.rect.x <= 0:
            self.velocity[0] = -self.velocity[0]

        if  self.rect.y >= constants.SCREEN_HEIGHT-constants.CLIENT_SIZE or self.rect.y <= 0:
            self.velocity[1] = -self.velocity[1]

        
        self.image.fill(self.color)
        self.text = str(self.counter).rjust(3)
        self.textsurface = pygame.font.Font(None,30).render(self.text, True, constants.BLACK)
        self.image.blit(self.textsurface,self.textrect)

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

    def shoppingEnd(self):
        """ Changing status when the client has finish"""
        self.color = constants.RED
        self.shoppingFinished = True

    def goCheckout(self, checkout):
        """ Go to checkout function, mooving the client to the nearest checkout available """
        nearestCheckout = min([e for e in checkout], key=lambda e: pow(e.rect.x-self.rect.x, 2) + pow(e.rect.y-self.rect.y, 2))
        if self.rect.x > nearestCheckout.rect.x :
            self.velocity[0] = -3
        if self.rect.x >= nearestCheckout.rect.x + constants.STORECHEKOUT_SIZE + (len(nearestCheckout.clientWaiting)*constants.CLIENT_SIZE) and self.rect.x <= nearestCheckout.rect.x + constants.STORECHEKOUT_SIZE + (len(nearestCheckout.clientWaiting)*constants.CLIENT_SIZE) + 10  :
            self.velocity[0] = 0
            nearestCheckout.clientWaiting.append(self)
            self.checkingOut = True
            #print("ok x")
        if self.rect.y > nearestCheckout.rect.y :
            self.velocity[1] = -1
        if self.rect.y < nearestCheckout.rect.y :
            self.velocity[1] = +1
        if self.rect.y >= nearestCheckout.rect.y and self.rect.y <= nearestCheckout.rect.y + constants.STORECHEKOUT_SIZE:
            self.velocity[1] = 0
            #print("ok y")