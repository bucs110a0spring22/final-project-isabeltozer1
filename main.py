import pygame
from src import controller #import controller

def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    #Sofia added:
    game = controller.Controller()
    game.mainloop() #from Pygame video tutorial https://binghamton.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=793548b8-248a-460a-9949-aba601564124
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######
   

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
