import pygame #this is going to be a button

class Hold(pygame.sprite.Sprite):
  def __init__(self,x,y,img_file): #pos is position, a tuple with x, y coordinates #pos argument?
    pygame.sprite.Sprite.__init__(self) #initialize sprite object
  #coding a button really
    self.image = pygame.image.load(img_file).convert_alpha()
    self.rect = self.image.get_rect() #creates rectangle based on image size
    self.rect.x = x
    self.rect.y = y
  #self.rect.x = pos[0]
  #self.rect.y = pos[0] #top left of screen
    #distribute holds randomly
    #as game coding progresses: have color-coded levels of holds\

    


#will need to add updated for button
#random forloop