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
        self.image.fill(constants.GREEN)

        self.isOpen = True
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        

    def update(self):
        if self.isOpen:
            self.image.fill(constants.GREEN)
        else:
            self.image.fill(constants.RED)
