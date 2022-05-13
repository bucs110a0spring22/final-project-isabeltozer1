import pygame
import random

class Climber(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name
        self.istired = False 

  #climber shakes when they're tired
    def tired(self):
      while True:
        self.rect.x += random.randrange(-1,1)

  #climber falls
    def falling(self):
      self.rect.x = 300
      self.rect.y = 380
      print("You fell! Try again")
      #might have to import new module to fall with physics, for now will just set myself to bottom

  #climber moves to a hold the user will click on
    def grab_hold(self,x,y):
        self.rect.x = x
        self.rect.y = y


