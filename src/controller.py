import sys
import pygame
import random
from src import climber
from src import rockwall
#from src import holds
from src import button


class Controller:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.num_holds = 0
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((200, 200, 200))  # set the background to grey
        pygame.font.init()  # you have to call this at the start, if you want to use this module.
        pygame.key.set_repeat(1, 50)  # initialize a held keey to act as repeated key strikes
        self.rockwall = rockwall.Rockwall(0,0,'assets/rockwall.png')
        self.climber = climber.Climber("Angela", 300, 300, "assets/climber.png")
        self.button1 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold.png')
        self.button2 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold.png')
        self.button3 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold.png')
        self.button4 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold.png')
        self.button5 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold.png')
        self.button6 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold.png')
        self.button7 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold.png')
        self.button8 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold.png')
        self.button9 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold.png')
        self.button10 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold.png')
        self.button11 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold2.png')
        self.button12 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold2.png')
        self.button13 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold2.png')
        self.button14 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold2.png')
        self.button15 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold2.png')
        self.button16 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold2.png')
        self.button17 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold2.png')
        self.button18 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold2.png')
        self.button19 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold2.png')
        self.button20 = button.Button(random.randrange(10, 630),random.randrange(10, 400),'assets/hold2.png')
        pygame.display.flip()
        self.state = "GAME"

    def mainLoop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def gameLoop(self):
        while self.state == "GAME":
            self.screen.blit(self.rockwall.image,self.rockwall.rect)
            self.screen.blit(self.climber.image,self.climber.rect)
            self.screen.blit(self.button1.image,self.button1.rect)
            self.screen.blit(self.button2.image,self.button2.rect)
            self.screen.blit(self.button3.image,self.button3.rect)
            self.screen.blit(self.button4.image,self.button4.rect)
            self.screen.blit(self.button5.image,self.button5.rect)
            self.screen.blit(self.button6.image,self.button6.rect)
            self.screen.blit(self.button7.image,self.button7.rect)
            self.screen.blit(self.button8.image,self.button8.rect)
            self.screen.blit(self.button9.image,self.button9.rect)
            self.screen.blit(self.button10.image,self.button10.rect)
            self.screen.blit(self.button11.image,self.button11.rect)
            self.screen.blit(self.button12.image,self.button12.rect)
            self.screen.blit(self.button13.image,self.button13.rect)
            self.screen.blit(self.button14.image,self.button14.rect)
            self.screen.blit(self.button15.image,self.button15.rect)
            self.screen.blit(self.button16.image,self.button16.rect)
            self.screen.blit(self.button17.image,self.button17.rect)
            self.screen.blit(self.button18.image,self.button18.rect)
            self.screen.blit(self.button19.image,self.button19.rect)
            self.screen.blit(self.button20.image,self.button20.rect)
            self.climber.update()
            
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                  if(self.button1.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button1.rect.x,self.button1.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                    #time_holding = current_time - start_hold_time
                    #while time_holding > 5000: #holding more than 5 seconds
                    #  self.climber.tired()
                    
                  elif(self.button2.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button2.rect.x,self.button2.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button3.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button3.rect.x,self.button3.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button4.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button4.rect.x,self.button4.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button5.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button5.rect.x,self.button5.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button6.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button6.rect.x,self.button6.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button7.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button7.rect.x,self.button7.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button8.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button8.rect.x,self.button8.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button9.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button9.rect.x,self.button9.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button10.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button10.rect.x,self.button10.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button11.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button11.rect.x,self.button11.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button12.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button12.rect.x,self.button12.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button13.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button13.rect.x,self.button13.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button14.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button14.rect.x,self.button14.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button15.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button15.rect.x,self.button15.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button16.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button16.rect.x,self.button16.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button17.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button17.rect.x,self.button17.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button18.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button18.rect.x,self.button18.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button19.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button19.rect.x,self.button19.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button20.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button20.rect.x,self.button20.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                if event.type == pygame.KEYDOWN:
                    self.climber.tired()
                  

                