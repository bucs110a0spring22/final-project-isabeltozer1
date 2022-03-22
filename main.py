import pygame
#import your controller

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

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
