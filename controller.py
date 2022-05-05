import pygame
import src.holds
import src.climber
import src.rockwall

class Controller: 
  def __init__(self):
     self.display = pygame.display.setmode((500,500),pygame.FULLSCREEN)
     self.hold = src.holds.Hold((250,250),"filename") #hold in center of screen
     self.STATE = "game"
    self.background.fill((211, 211, 211))  # set the background to light grey
        pygame.font.init()  # you have to call this at the start, if you want to use this module.

     #now loading sprites we need, copied from lab 10
    self.enemies = pygame.sprite.Group()
        num_holds = 100
        for i in range(num_holds):
            x = random.randrange(100, 400)
            y = random.randrange(100, 400)
            self.holds.add(holds.Hold(self,pos,fn))
          
        self.climber = climber.Climber("Angela", 50, 80, "climber.png")
        self.all_sprites = pygame.sprite.Group((self.hero,) + tuple(self.enemies))
        #self.shield_sprites = pygame.sprite.Group(self.shieldturtle)
     

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