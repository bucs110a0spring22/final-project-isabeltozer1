import pygame
from src import controller #import controller

def list_maker():
  mylist = [ ]
  for i in range(1,5):
    a_number = int(input("enter a number"))
    mylist.append(a_number)
  return mylist

def main():
    pygame.init()
    listmaker()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######
   #Sofia added:
    #game = Controller()
    #game.mainloop() #from Pygame video tutorial https://binghamton.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=793548b8-248a-460a-9949-aba601564124

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
