import pygame
from src import controller #import controller

def main():
    main_window = controller.Controller()
    main_window.mainLoop()
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######
   

#if __name__ == '__main__':
main()
