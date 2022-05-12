import pygame
import random
from src import hold
from src import climber
#import src.rockwall

class Controller: 
   def __init__(self):
     pygame.init()
     self.screen = pygame.display.set_mode((500,500),pygame.FULLSCREEN)
     self.background = pygame.Surface(self.screen.get_size()).convert()
     self.background.fill((211, 211, 211))
     pygame.font.init()
     
     self.holds = pygame.sprite.Group()
     num_holds = 100
     for i in range(num_holds):
       x = random.randrange(100, 400)
       y = random.randrange(100, 400)
       self.holds.add(hold.Hold(x,y,'assets/hold.jpg')) 
     self.climber = climber.Climber("Angela", 50, 80, "assets/climber.jpg")
     self.all_sprites = pygame.sprite.Group((self.climber,) + tuple(self.holds))
     self.STATE = "game"
     #self.hold = src.holds.Hold((250,250),"hold.png") #hold in center of screen   
     #self.background.fill((211, 211, 211))  # set the background to light grey, for now that's our boulder wall
     

   def mainloop(self):
     while True:
       if self.STATE == "game":
         self.gameloop()
       elif self.STATE == "exit":
         self.exitloop()

   def gameloop(self):
     while self.STATE == "game":
       for event in pygame.event.get():
         if event.type == pygame.QUIT:
           self.STATE = "exit"
          #reset climber position next:
         elif event.type == pygame.BUTTON_X1:
           self.climber.move() #will have to make this function yeah...
         self.climber.update()

   def exitloop(self):
     pygame.quit()
     exit()

# I want to add a "try again" option if climber falls