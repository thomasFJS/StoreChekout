import pygame

import constants


class StoreCheckout(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([constants.STORECHEKOUT_SIZE, constants.STORECHEKOUT_SIZE])
        self.color = constants.GREEN
        self.image.fill(self.color)
        self.clientWaiting = []
        self.text = "-"
        self.textsurface = pygame.font.Font(None,30).render(self.text, True, constants.WHITE)
        self.textrect = self.textsurface.get_rect(center=self.image.get_rect().center)
        

        self.isOpen = True
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        

    def update(self):
        if self.isOpen:
            self.color = constants.GREEN
        else:
            self.color = constants.RED

        self.image.fill(self.color)
        if(self.clientWaiting):
            self.text = str(self.clientWaiting[0].timeToCheckout)
            self.textsurface = pygame.font.Font(None,30).render(self.text, True, constants.BLACK)
            self.image.blit(self.textsurface,self.textrect)
