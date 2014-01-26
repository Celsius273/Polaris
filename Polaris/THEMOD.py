# This is a module for the ship
# It includes ship movement, shooting, and health algorithms
# As well as polarity, that's the most important part
# A separate(maybe) module will be made for the enemies
# As for the bosses, that's also separate
import pygame, sys,os, time, random

from pygame.locals import * 
from pygame.color import THECOLORS
import platform, os

def text(text,color,x,y):
    text = myfont.render(text, True, THECOLORS[color])
    screen.blit(text, (x,y))
def line(color, a, b, c, d,):
    pygame.draw.line(screen, THECOLORS[color], (a, b), (c, d))
def circle(color, x, y, radius):
    pygame.draw.line(screen, THECOLORS[color], (x, y), radius)
def rect(color, a, b, c, d):
    pygame.draw.rect(screen, THECOLORS[color], (a, b, c, d))
def img(path, x, y):
    img_surface = pygame.image.load(os.path.join('sprites', path))
    screen.blit(img_surface, (x,y))
def image_get(folder, image):
    pygame.image.load(os.path.join(folder, image))
def fill(color):
    screen.fill(THECOLORS[color])
def flip():
    pygame.display.flip()
def blit(image, x, y):
    screen.blit(image, (x,y))

class ship:
    def __init__(self, name):
        self.name=name 
        self.lives=5 
        self.health=10
        self.alive=True
        self.polarity='blue'
        self.shoot=True
        self.points=0
        self.pos=[225, 450]
        self.move=[5, 5]
        self.cd = 12
    
    def hit(self):
        self.health -= 1
        self.cd = 12
        if self.health == 0:
            self.lives -=1
            self.health = 5
            self.cd = 24
        if self.lives == 0 and self.health == 0:
            self.alive = False 

##Below are the enemy classes.....
            
class e1_1:
    def __init__(self, x, y, polarity, xvelo, yvelo, sl, sw, n, t):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("1e1.png")
        self.health=8
        self.polarity='blue'
        self.xvelo = xvelo
        self.yvelo = yvelo
        self.sl=sl
        self.sw=sw
        self.n=n
        self.t=t

    def hit(self):
        self.health -= 2
        if self.health <= 0:
            self.alive = False

    def hit2(self):
        self.health -= 4
        if self.health <= 0:
            self.alive = False
            
class e1_1b:
    def __init__(self, x, y, polarity, xvelo, yvelo,sl,sw,n, t):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("1e1b.png")
        self.health=8
        self.polarity='brown'
        self.xvelo = xvelo
        self.yvelo = yvelo
        self.sl=sl
        self.sw=sw
        self.n=n
        self.t=t
    
    def hit(self):
        self.health -= 2
        if self.health <= 0:
            self.alive = False
            
    def hit2(self):
        self.health -= 4
        if self.health <= 0:
            self.alive = False
            
class e1_2:
    def __init__(self, x, y, polarity, xvelo, yvelo,sl,sw,n, t):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("1e2.png")
        self.health=5
        self.polarity='blue'
        self.xvelo = xvelo
        self.yvelo = yvelo
        self.sl=sl
        self.sw=sw
        self.n=n
        self.t=t
        
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.alive = False
            
    def hit2(self):
        self.health -= 2
        if self.health <= 0:
            self.alive = False
            
class e1_2b:
    def __init__(self, x, y, polarity, xvelo, yvelo,sl,sw,n, t):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("1e2b.png")
        self.health=5
        self.polarity='brown'
        self.xvelo = xvelo
        self.yvelo = yvelo
        self.sl=sl
        self.sw=sw
        self.n=n
        self.t=t
        
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.alive = False
            
    def hit2(self):
        self.health -= 2
        if self.health <= 0:
            self.alive = False
            
class e1_3:
    def __init__(self, x, y, polarity, xvelo, yvelo,sl,sw,n, t):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("1e3.png")
        self.health=36
        self.polarity='blue'
        self.xvelo = xvelo
        self.yvelo = yvelo
        self.sl=sl
        self.sw=sw
        self.n=n
        self.t=t
        
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.alive = False
            
    def hit2(self):
        self.health -= 3
        if self.health <= 0:
            self.alive = False
            
class e1_4b1:
    def __init__(self, x, y, polarity, xvelo, yvelo,sl,sw,n, t):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("1e4b-1.png")
        self.health=4
        self.polarity='brown'
        self.xvelo = xvelo
        self.yvelo = yvelo
        self.sl=sl
        self.sw=sw
        self.n=n
        self.t=t
        
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.alive = False
            
    def hit2(self):
        self.health -= 2
        if self.health <= 0:
            self.alive = False
            
class e1_4b2:
    def __init__(self, x, y, polarity, xvelo, yvelo,sl,sw,n, t):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("1e4b-2.png")
        self.health=4
        self.polarity='brown'
        self.xvelo = xvelo
        self.yvelo = yvelo
        self.sl=sl
        self.sw=sw
        self.n=n
        self.t=t
        
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.alive = False
            
    def hit2(self):
        self.health -= 2
        if self.health <= 0:
            self.alive = False
            
class e1_5:
    def __init__(self, x, y, polarity, xvelo, yvelo,sl,sw,n, t):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("1e5.png")
        self.health=2
        self.polarity='blue'
        self.xvelo = xvelo
        self.yvelo = yvelo
        self.sl=sl
        self.sw=sw
        self.n=n
        self.t=t
        
    def hit(self):
        self.health -= 0
        if self.health <= 0:
            self.alive = False
            
    def hit2(self):
        self.health -= 2
        if self.health <= 0:
            self.alive = False
            
class e1_5b:
    def __init__(self, x, y, polarity, xvelo, yvelo,sl,sw,n, t):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("1e5b.png")
        self.health=2
        self.polarity='brown'
        self.xvelo = xvelo
        self.yvelo = yvelo
        self.sl=sl
        self.sw=sw
        self.n=n
        self.t=t
        
    def hit(self):
        self.health -= 0
        if self.health <= 0:
            self.alive = False
            
    def hit2(self):
        self.health -= 2
        if self.health <= 0:
            self.alive = False
            
class e1_6b:
    def __init__(self, x, y, polarity, xvelo, yvelo,sl,sw,n, t):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("1e6b.png")
        self.health=12
        self.polarity='brown'
        self.xvelo = xvelo
        self.yvelo = yvelo
        self.sl=sl
        self.sw=sw
        self.n=n
        self.t=t
        
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.alive = False
            
    def hit2(self):
        self.health -= 3
        if self.health <= 0:
            self.alive = False
            
class e1_7:
    def __init__(self, x, y, polarity, xvelo, yvelo,sl,sw,n, t):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("1e7.png")
        self.health=6
        self.polarity='blue'
        self.xvelo = xvelo
        self.yvelo = yvelo
        self.sl=sl
        self.sw=sw
        self.n=n
        self.t=t
        
    def hit(self):
        self.health -= 3
        if self.health <= 0:
            self.alive = False
            
    def hit2(self):
        self.health -= 6
        if self.health <= 0:
            self.alive = False
            
class e1_8:
    def __init__(self, x, y, polarity, xvelo, yvelo,sl,sw,n, t):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("1e8.png")
        self.health=32
        self.polarity='blue'
        self.xvelo = xvelo
        self.yvelo = yvelo
        self.sl=sl
        self.sw=sw
        self.n=n
        self.t=t
        
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.alive = False
            
    def hit2(self):
        self.health -= 4
        if self.health <= 0:
            self.alive = False
            
##Below are the enemy bullet classes

class b1:
    def __init__(self, x, y, polarity, xvelo, yvelo):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("b1.png")
        self.polarity='blue'
        self.xvelo = xvelo
        self.yvelo = yvelo
        
    def collide(self):
        self.alive = False
        
    def absorb(self):
        self.alive = False
        
class b1b:
    def __init__(self, x, y, polarity, xvelo, yvelo):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("b1b.png")
        self.polarity='brown'
        self.xvelo = xvelo
        self.yvelo = yvelo
        
    def collide(self):
        self.alive = False
        
    def absorb(self):
        self.alive = False
        
class b2:
    def __init__(self, x, y, polarity, xvelo, yvelo):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("b2.png")
        self.polarity='blue'
        self.xvelo = xvelo
        self.yvelo = yvelo
        
    def collide(self):
        self.alive = False
        
    def absorb(self):
        self.alive = False
        
class b2b:
    def __init__(self, x, y, polarity, xvelo, yvelo):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("b2b.png")
        self.polarity='brown'
        self.xvelo = xvelo
        self.yvelo = yvelo
        
    def collide(self):
        self.alive = False
        
    def absorb(self):
        self.alive = False
        
class b3:
    def __init__(self, x, y, polarity, xvelo, yvelo):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("b3.png")
        self.polarity='blue'
        self.xvelo = xvelo
        self.yvelo = yvelo
        
    def collide(self):
        self.alive = False
        
    def absorb(self):
        self.alive = False
        
class b3b:
    def __init__(self, x, y, polarity, xvelo, yvelo):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("b3b.png")
        self.polarity='brown'
        self.xvelo = xvelo
        self.yvelo = yvelo
        
    def collide(self):
        self.alive = False
        
    def absorb(self):
        self.alive = False
        
class b4:
    def __init__(self, x, y, polarity, xvelo, yvelo):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("b4.png")
        self.polarity='blue'
        self.xvelo = xvelo
        self.yvelo = yvelo
        
    def collide(self):
        self.alive = False
        
    def absorb(self):
        self.alive = False
        
class boss1:
    def __init__(self, x, y, polarity, xvelo, yvelo, sl,sw,n, t):
        self.alive = True
        self.xpos = x
        self.ypos = y
        self.img = pygame.image.load("boss1.png")
        self.health=4000
        self.polarity='non'
        self.xvelo = xvelo
        self.yvelo = yvelo
        self.sl=sl
        self.sw=sw
        self.n=n
        self.t=t
        
    def hit(self):
        self.health -= 3
        if self.health <= 0:
            self.alive = False
        
        