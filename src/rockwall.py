import pygame

class Rockwall(pygame.sprite.Sprite):
  def __init__(self,x,y,image):
    #pygame.sprite.Sprite.__init__(self)
    #self.image =  pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(), (640,480))
    self.image =  pygame.image.load(image).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    