import pygame
import src.holds
import src.climber
import src.rockwall

def__init__(self):
   self.display = pygame.display.setmode((500,500),pygame.FULLSCREEN)
   self.hold = src.holds.Hold((250,250),"filename") #hold in center of screen
   self.STATE = "game"

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
           self.STATE == "exit"
        #reset climber position next:
         elif event.type == pygame.BUTTON_X1:
           self.climber.move() #will have to make this function
         self.climber.update()

   def exitloop(self):
     pygame.quit()
     exit()

# I want to add a "try again" option if climber falls