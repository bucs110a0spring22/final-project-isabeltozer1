#climber, arms legs, body
#Climber class that has list of all the individual body parts
#  Arm
#  Leg
#  Head and body
#  Utility class that helps the arm moves in unison
    #not sure ab that part


class Climber(pygame.sprite.Sprite):

  def __init__(self, name, x, y, img_file):
    
    pygame.sprite.Sprite.__init__(self)
    #self.climber = climber
    #self.rightarm = rightarm 
    #self.rightleg = rightleg
    #self.leftarm = leftarm
    #self.leftleg = leftleg
    self.image = pygame.image.load(img_file).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    #set other attributes
    self.name = name #why do I need this?
    self.speed = 3
    self.health = 3

    #some methods to move our climber (haven't considered moving arms/legs separately yet)
    def move_hold(self):
        self.rect.y -= self.speed #will change later
        self.rect.y += self.speed

