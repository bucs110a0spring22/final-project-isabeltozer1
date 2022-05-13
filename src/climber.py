import pygame
#model
class Climber(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name
        self.tired = False 

    def falling(self):
      self.rect.x = 300
      self.rect.y = 380
      #pass #might have to import new module to fall with physics, for now will just set myself to bottom


    def grab_hold(self,x,y):
        self.rect.x = x
        self.rect.y = y


