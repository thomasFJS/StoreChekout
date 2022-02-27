import pygame

import constants


class Infos(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, checkouts, clients):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent

        #All labels text 
        self.info1 = "Caisses : "
        self.info2 = "Temps avant ouverture : "
        self.info3 = "Clients sans caisse : "
        self.info4 = "Nombre de clients : "
        self.info5 = "Heure : "

        self.label = []
        #All values (goes with the labels)
        self.nbCheckouts = 0
        self.timeBeforeOpening = 0
        self.clientsWithoutCheckout = 0
        self.NbClients = 0
        self.Hours = 0


        #all clients and checkout
        self.all_checkout = checkouts
        self.all_clients = clients

        self.image = pygame.Surface([constants.INFOS_SIZE, constants.INFOS_SIZE])

        self.image.fill(constants.WHITE)
        self.text = "-"
        self.textsurface = pygame.font.Font(None,20).render(self.text, True, constants.BLACK)
        self.textrect = self.textsurface.get_rect(center=self.image.get_rect().center)
        self.textrect.left = 0
        self.textrect.top = 0
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 500
        

    def update(self):
        label = []
        self.nbCheckouts = 0
        self.timeBeforeOpening = 0
        self.clientsWithoutCheckout = 0
        self.NbClients = 0

        for c in self.all_checkout:
            if c.isOpen:
                self.nbCheckouts+=1
                
        label.append(pygame.font.Font(None,20).render(self.info1 + str(self.nbCheckouts) + " / " + str(len(self.all_checkout)), True, constants.BLACK))
        
        #TO DO 
        label.append(pygame.font.Font(None,20).render(self.info2, True, constants.BLACK))

        for client in self.all_clients:
            if client.checkingOut == False and client.shoppingFinished == True:
                self.clientsWithoutCheckout +=1

        label.append(pygame.font.Font(None,20).render(self.info3 + str(self.clientsWithoutCheckout), True, constants.BLACK))

        self.NbClients = len(self.all_clients)
        label.append(pygame.font.Font(None,20).render(self.info4 + str(self.NbClients), True, constants.BLACK))
        
        label.append(pygame.font.Font(None,20).render(self.info5 + str(self.Hours), True, constants.BLACK))

        self.image.fill(constants.WHITE)
        
        #self.text = self.info1 + '\n' + self.info2 + '\n' + self.info3 + '\n' + self.info4 + '\n' + self.info5
        #print(self.text)
        for line in range(len(label)):
            self.image.blit(label[line], (self.textrect.x, self.textrect.y+(line*20)+(15*line)))
        #self.textsurface = pygame.font.Font(None,20).render(self.text, True, constants.BLACK)
        #self.image.blit(self.textsurface,self.textrect)


    def updateValues(self, checkouts, clients, hours):
        self.all_checkout = checkouts
        self.all_clients = clients
        self.Hours = hours
