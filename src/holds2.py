import pygame #this is going to be a button
import random

class Hold2(pygame.sprite.Sprite):
  def __init__(self,x1,x2,y1,y2,img_file): #pos is position, a tuple with x, y coordinates #pos argument?
    pygame.sprite.Sprite.__init__(self) #initialize sprite object
  #coding a button really
    self.image = pygame.image.load(img_file).convert_alpha()
    self.rect = self.image.get_rect() #creates rectangle based on image size
    self.rect.x = random.randrange(x1, x2)
    self.rect.y = random.randrange(y1, y2)
  #self.rect.x = pos[0]
  #self.rect.y = pos[0] #top left of screen
    #distribute holds randomly
    #as game coding progresses: have color-coded levels of holds\

   