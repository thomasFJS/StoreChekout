import pygame

import constants

from random import randint
 
class Client(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([constants.CLIENT_SIZE, constants.CLIENT_SIZE])
        self.image.fill(constants.WHITE)
 
        self.counter = randint(randint(constants.MIN_TIME_IN_STORE_FROM,constants.MIN_TIME_IN_STORE_TO),randint(constants.MAX_TIME_IN_STORE_FROM,constants.MAX_TIME_IN_STORE_TO))
        self.text = str(self.counter).rjust(3)
        self.textsurface = pygame.font.Font(None,30).render(self.text, True, constants.BLACK)
        self.textrect = self.textsurface.get_rect(center=self.image.get_rect().center)
        self.image.blit(self.textsurface,self.textrect)
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)
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

        self.text = str(self.counter).rjust(3)
        print(self.counter)

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

    