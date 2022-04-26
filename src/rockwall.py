import pygame

class Rockwall(pygame.sprite.Sprite):
  def__init__(self,pos,fn): #pos is position, a tuple with x, y coordinates
  pygame.sprite.Sprite__init__(self) #initialize sprite object
  #coding a button really
  self.image = pygame.image.load(fn) #big image
  self.rect = self.image.get_rect() #creates rectangle based on image size
  self.rect.x = pos[0]
  self.rect.y = pos[0] #top left of screen
    #distribute holds randomly
  self.direction = 'd' #wall will scroll down as climber moves up
  self.direction = 'u' #wall scroll up if climber falls
    #as game coding progresses: have color-coded levels of holds

  def update(self):
    #change direction, but this is a result of climber event so might have to do this in controller
    #moving up and down:
   if self.direction == 'd':
     self.rect.y -= 1
   elif self.direction == 'u':
     self.rect.y += 1 
   