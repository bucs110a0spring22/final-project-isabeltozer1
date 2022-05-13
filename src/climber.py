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
        self.tootired = False

  #climber shakes when they're tired
    def fatigue(self, start_time):
      self.istired = False
      current_time = pygame.time.get_ticks()
      time_holding = current_time - start_time
      if time_holding > 5000:
        self.istired = True
        print("You're tired! You only have a little time left to get to the top!")
        if time_holding > 10000:
          self.tootired = True

  #climber falls
    def falling(self):
      self.rect.x = 300
      self.rect.y = 300
      print("You fell! Try again")
      self.istired = False
      #might have to import new module to fall with physics, for now will just set myself to bottom

  #climber moves to a hold the user will click on
    def grab_hold(self,x,y):
        self.rect.x = x
        self.rect.y = y
        self.istired = False

    def update(self):
      if self.tootired == True:
        self.rect.x = 300
        self.rect.y = 300
        print("You fell! Try again")
      elif self.istired == True:
        options = [-1,0,1]
        self.rect.x += random.choice(options) #shake if tired
      else:
        pass


