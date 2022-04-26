import pygame

class Hold(pygame.sprite.Sprite):
  def__init__(self,pos,fn): #pos is position, a tuple with x, y coordinates
  pygame.sprite.Sprite__init__(self) #initialize sprite object
  #coding a button really
  self.image = pygame.image.load(fn)
  self.rect = self.image.get_rect() #creates rectangle based on image size
  self.rect.x = pos[0]
  self.rect.y = pos[0] #top left of screen
    #distribute holds randomly
    #as game coding progresses: have color-coded levels of holds
   