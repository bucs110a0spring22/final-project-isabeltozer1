import pygame
#import random
#from src import hold
from src import climber
#from src import button
from src import holds2
#import src.rockwall

class Controller:
  
  def __init__(self, width=640, height=480):
    pygame.init()
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((self.width, self.height))
    self.background = pygame.Surface(self.screen.get_size()).convert()
    self.background.fill((200, 200, 200))  # set the background to white
    pygame.font.init()  # you have to call this at the start, if you want to use this module.
    pygame.key.set_repeat(1, 50)  # initialize a held keey to act as repeated key strikes

    #self.holds = pygame.sprite.Group()
    #num_holds = 20
    #for i in range(num_holds):
    #    x = random.randrange(40, 600)
    #    y = random.randrange(50, 300)
    #    self.holds.add(hold.Hold(x,y, 'assets/hold.png'))
    self.hold1 = holds2.Hold2(40,600,50,300,'assets/hold.png')
    self.hold2 = holds2.Hold2(40,600,50,300,'assets/hold.png')
    self.hold3 = holds2.Hold2(40,600,50,300,'assets/hold.png')
    self.hold4 = holds2.Hold2(40,600,50,300,'assets/hold.png')
    self.hold5 = holds2.Hold2(40,600,50,300,'assets/hold.png')
    self.hold6 = holds2.Hold2(40,600,50,300,'assets/hold.png')
    self.hold7 = holds2.Hold2(40,600,50,300,'assets/hold.png')
    self.hold8 = holds2.Hold2(40,600,50,300,'assets/hold.png')
    self.hold9 = holds2.Hold2(40,600,50,300,'assets/hold.png')
    self.hold10 = holds2.Hold2(40,600,50,300,'assets/hold.png')
    self.climber = climber.Climber("Angela", 50, 80, "assets/climber.png")
    #self.button = #button.Button((250,250),'assets/hold.png')
    self.all_sprites = pygame.sprite.Group((self.climber,))#,self.hold1,self.hold2,self.hold3,self.hold4,self.hold5,self.hold6,self.hold7,self.hold8,self.hold9,self.hold10)) #+ tuple(self.holds))
    self.STATE = "game"
     #self.hold = src.holds.Hold((250,250),"hold.png") #hold in center of screen   
     #self.background.fill((211, 211, 211))  # set the background to light grey, for now that's our boulder wall
     

  def mainLoop(self):
    while True:
      if self.STATE == "game":
        self.gameloop()
      elif self.STATE == "exit":
        self.exitloop()

  def gameloop(self):
    while self.STATE == "game":
      #self.all_sprites.draw(self.screen)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.STATE = "exit"
        #reset climber position next:
        elif event.type == pygame.KEYDOWN:
          self.screen.blit(self.background, (0, 0))
          self.all_sprites.draw(self.screen)#idk
          pygame.display.flip()
         #elif event.type == pygame.MOUSEBUTTONDOWN:  #BUTTON_X1:
           #if(self.holds.rect.collidepoint(event.pos)):
    #        self.climber.move() #will have to make this function yeah...
   #         self.climber.update()

  def exitloop(self):
    pygame.quit()
    exit()

# I want to add a "try again" option if climber falls