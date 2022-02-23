import pygame

import constants

from random import randint
 
class Client(pygame.sprite.Sprite):
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.color = constants.WHITE

        self.shoppingFinished = False

        self.image = pygame.Surface([constants.CLIENT_SIZE, constants.CLIENT_SIZE])
        self.image.fill(self.color)
 
        self.counter = randint(randint(constants.MIN_TIME_IN_STORE_FROM,constants.MIN_TIME_IN_STORE_TO),randint(constants.MAX_TIME_IN_STORE_FROM,constants.MAX_TIME_IN_STORE_TO))
        self.baseCounter = self.counter
        
        
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
        #print(self.counter)

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

    def shoppingEnd(self):
        self.color = constants.RED
        self.shoppingFinished = True

    def goCheckout(self, enemies):
        nearestCheckout = min([e for e in enemies], key=lambda e: pow(e.rect.x-self.rect.x, 2) + pow(e.rect.y-self.rect.y, 2))
        if self.rect.x > nearestCheckout.rect.x :
            self.velocity[0] = -1
        if self.rect.x < nearestCheckout.rect.x :
            self.velocity[0] = +1
        if self.rect.x == nearestCheckout.rect.x :
            self.velocity[0] = 0
            print("ok")
        if self.rect.y > nearestCheckout.rect.y :
            self.velocity[1] = -1
        if self.rect.y < nearestCheckout.rect.y :
            self.velocity[1] = +1
        if self.rect.y == nearestCheckout.rect.y :
            self.velocity[1] = 0
            print("ok")