## Polarity shooter game
## For ICS201, summative project
## By Kelvin Jiang
## January, 7, 2011

import pygame, sys,os, time, random, THEMOD

from pygame.locals import *
from pygame.color import THECOLORS

from THEMOD import ship, e1_1, e1_1b, e1_2, e1_2b, e1_3, e1_4b1, e1_4b2, e1_5, e1_5b, e1_6b , e1_7, e1_8, b1, b1b, b2, b2b, b3, b3b, b4, boss1

## If you get the no available video device error, copy and paste the below code ##
import platform, os
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
### If you get the no available video device error, copy and paste the above code ###

# This is the basic setup procedure
pygame.init() 
clock=pygame.time.Clock()
window = pygame.display.set_mode((450, 600)) 
pygame.display.set_caption('ICS201 Summative') 
screen = pygame.display.get_surface()
screen.fill(THECOLORS['black'])

#Font setup

myfont = pygame.font.Font("robotaur.ttf", 20)
titlefont = pygame.font.Font("bgothm.ttf", 80)
selfont = pygame.font.Font("bgothm.ttf", 30)
selfont2 = pygame.font.Font("bgothm.ttf", 16)

test=pygame.display.get_driver()
#Setup ends

##Basic functions, these are just to shorten the main pygame functions
def text(text, font, color,x,y):
    text = font.render(text, True, THECOLORS[color])
    screen.blit(text, (x,y))
    
def text2(text,font, color, x, y):
    text = font.render(text, True, color)
    screen.blit(text, (x,y))
    
def line(color, a, b, c, d,):
    pygame.draw.line(screen, THECOLORS[color], (a, b), (c, d))
def circle(color, x, y, radius):
    pygame.draw.line(screen, THECOLORS[color], (x, y), radius)
def rect(color, a, b, c, d):
    pygame.draw.rect(screen, THECOLORS[color], (a, b, c, d))
def rect2(color, a, b, c, d):
    pygame.draw.rect(screen, color, (a, b, c, d))
def rect3(color, a, b, c, d):
    pygame.draw.rect(screen, color, (a, b, c-a, d-b))
def img(path, x, y):
    img_surface = pygame.image.load(os.path.join('sprites', path))
    screen.blit(img_surface, (x,y))
def blit(image, x, y):
    screen.blit(image, (x,y))
def image_get(folder, image):
    pygame.image.load(os.path.join(folder, image))
def fill(color):
    screen.fill(THECOLORS[color])
def flip():
    pygame.display.flip()
    
def avg(a, b): ##function for the average of 2 integers
    v = (float(a+b)/2)
    return v
                    
def aimx(x, x2, y, y2, c): #The x velocity of a shot aimed towards the player
    xv = ((x-x2)/avg(abs(float(x-x2)), abs(float(y-y2))))*c
    
    return xv

def aimy(x, x2, y, y2, c): #and now for the y velocity
    yv = ((y-y2)/avg(abs(float(x-x2)), abs(float(y-y2))))*c
    
    return yv


fil=open("highscores.txt","r")

dat=fil.readlines()

f=0


##Initializing the lists that store the highscores
nlist=[]
sclist=[]

nlist2=[]
sclist2=[]

name=[]

stname=''

if dat !=[]:
    while f<len(dat):
        t=dat[f].split('\t')
        #That's the only use for t, it is now useless
        nlist.append(str(t[0]))
        sclist.append(int(t[1]))        
        f+=1
        

##Setup for basic functions ends

##Setting up accumulators

#This is for the amount of frames elapseds
tloop=0

#These 3 are file related
sc=0
sor=0
fc=0

ps=0

blist=[] #List for your bullets

elist=[] #List for enemies

belist=[] #List for bullets shot by enemies

exlist=[] #Lists for explosions
exlist2=[]
exb1 = pygame.image.load('exb1_1.png') #Loading explosions for the enemies
exb2 = pygame.image.load('exb2_1.png')

bpos=[225, 450]

player=ship("kelvin")

#Loading all the images
if player.polarity == 'blue':
    theship=pygame.image.load('player_blue.png')
elif player.polarity == 'brown':
    theship=pygame.image.load('player_brown.png')
    
lbullet=pygame.image.load('bullet_bluel.png')
lbullet2=pygame.image.load('bullet_brownl.png')
rbullet=pygame.image.load('bullet_bluer.png')
rbullet2=pygame.image.load('bullet_brownr.png')

pause=pygame.image.load('pause.png')

star=pygame.image.load('star.png')
slist=[]

startscreen=pygame.image.load('start.png')

help=pygame.image.load('helpscreen.png')
help2=pygame.image.load('helpscreen2.png')

over=pygame.image.load('helpbg.png')


#Setting up the final variables
pygame.key.set_repeat(5, 2)
running= True
mode='start'
prevmode = 0

bossl=[]

bossalive = False

try:
    while running:
        #Different music plays depending on the mode you're in
        if mode == 'start' and prevmode != mode:  
            pygame.mixer.music.stop()
            pygame.mixer.music.load('menu.mp3')
            pygame.mixer.music.play(-1)
            prevmode = mode
            
        if mode == 'game' and prevmode != mode:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('stage1.mp3')
            pygame.mixer.music.play(-1)
            prevmode = mode

        if mode == 'boss1' and prevmode != mode:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('boss1theme.mp3')
            pygame.mixer.music.play(-1)
            prevmode = mode
            
        screen.fill(THECOLORS['black'])
        #Variables tracking the mouse and the keyboard
        mpos=pygame.mouse.get_pos()
        
        butt = pygame.mouse.get_pressed()
        key=pygame.key.get_pressed()
        if mode=='start':
            sc=0
            pygame.key.set_repeat(5, 2)
            blit(startscreen, 0, 0)
            #Blitting the graphics on the screen
            text2('Polaris', titlefont ,(255, 150, 0), 60, 50)
            
            rect3((0, 0, 0), 152, 152, 298, 223)
            rect3((0, 255, 50), 160, 160, 290, 215)
            text2('Start', selfont, (0, 0, 64), 180, 170)
            
            rect3((0, 0, 0), 152, 232, 298, 303)
            rect3((0, 255, 50), 160, 240, 290, 295)
            text2('Hiscores', selfont2, (0, 0, 64), 180, 260)
            
            rect3((0, 0, 0), 152, 312, 298, 383)
            rect3((0, 255, 50), 160, 320, 290, 375)
            text2('Help', selfont, (0, 0, 64), 180, 330)
            
            rect3((0, 0, 0), 152, 392, 298, 463)
            rect3((0, 255, 50), 160, 400, 290, 455)
            text2('Credits', selfont, (0, 0, 64), 160, 410)
            
            rect3((0, 0, 0), 390, 560, 440, 590)
            rect3((255, 25, 0), 392, 562, 438, 588)
            text2('Quit', selfont2, (0, 0, 64), 395, 565)
            
            #this makes the buttons larger when you mouse over them
            if 152 < mpos[0] < 298 and 152 < mpos[1] < 223:
                rect3((0, 0, 0), 150, 150, 300, 225)
                rect3((0, 255, 50), 158, 158, 292, 217)
                text2('Start', selfont, (0, 0, 64), 180, 170)
                
            if 152 < mpos[0] < 298 and 232 < mpos[1] < 303:
                rect3((0, 0, 0), 150, 230, 300, 305)
                rect3((0, 255, 50), 158, 238, 292, 297)
                text2('Hiscores', selfont2, (0, 0, 64), 180, 260)
                
            if 152 < mpos[0] < 298 and 312 < mpos[1] < 383:
                rect3((0, 0, 0), 150, 310, 300, 385)
                rect3((0, 255, 50), 158, 318, 292, 377)
                text2('Help', selfont, (0, 0, 64), 180, 330)
                
                #Commands for clicking on the buttons
            if 152 < mpos[0] < 298 and 152 < mpos[1] < 223 and butt ==(1, 0, 0):
                mode='game'
                
            if 152 < mpos[0] < 298 and 232 < mpos[1] < 303 and butt ==(1, 0, 0):
                mode = 'hiscore'
            
            if 152 < mpos[0] < 298 and 312 < mpos[1] < 383 and butt ==(1, 0, 0):
                mode = 'help'
                
            if 390 < mpos[0] < 440 and 560 < mpos[1] < 590 and butt ==(1, 0, 0):
                sys.exit()
            
            flip()
                
            events=pygame.event.get()
            for e in events: 
                if e.type == QUIT:
                    running=False   # Stop the program, it's detected quit...
        
        if mode=='help' or mode == 'help2':
            if mode == 'help':
                
                blit(help, 0, 0)
                
            if mode == 'help2':
                blit(help2, 0, 0)
                        
            rect3((0, 0, 0), 20, 30, 70, 60)
            rect3((255, 25, 0), 22, 32, 68, 58)
            text2('Back', selfont2, (0, 0, 64), 25, 35)
            
            if 20 < mpos[0] < 70 and 30 < mpos[1] < 60 and butt ==(1, 0, 0):
                mode = 'start'
            
            events=pygame.event.get()
            for e in events: 
                if e.type == QUIT:
                    running=False   # Stop the program, it's detected quit...
            flip()
            
        if mode == 'hiscore':
            ps=0
            blit(over, 0, 0)
            
            while ps <10:
                text2(nlist[ps], selfont, (0, 255, 0),50, (ps*40)+80)
                
                text2(str(sclist[ps]), selfont, (128, 0, 255),290, (ps*40)+80)
                
                ps+=1
            
            rect3((0, 0, 0), 20, 30, 70, 60)
            rect3((255, 25, 0), 22, 32, 68, 58)
            text2('Back', selfont2, (0, 0, 64), 25, 35)
            
            if 20 < mpos[0] < 70 and 30 < mpos[1] < 60 and butt ==(1, 0, 0):
                mode = 'start'
            
            events=pygame.event.get()
            for e in events: 
                if e.type == QUIT:
                    running=False   # Stop the program, it's detected quit...
            flip()
            
            
        if mode=='game' or mode == 'boss1':
            #These are the victory and loss conditions for the player
            if player.lives==0:
                mode='over'
                
            if tloop> 4200 and bossalive == False:
                mode='win'
                pygame.key.set_repeat(5, 2)
                
                #Loading the images for the player, includes main images and images after you get hit
            if player.polarity == 'blue' and player.cd == 0:
                theship=pygame.image.load('player_blue.png')
            elif player.polarity == 'blue' and player.cd > 0:
                theship=pygame.image.load('player_blue2.png')
            elif player.polarity == 'brown' and player.cd == 0:
                theship=pygame.image.load('player_brown.png')
            elif player.polarity == 'brown' and player.cd > 0:
                theship=pygame.image.load('player_brown2.png')
                
            ##Initializing randomizers for determining enemy positions when they spawn
            xposenemy = random.randint(15, 435)
            
            ytop = random.randint(15, 90)
            
            xcenter = random.randint(115, 335)
            
            ##This is a long series of code that determines when enemies spawn and which enemies will spawn, it includes all the information about the enemy
            if tloop % random.randint(80, 90) == 0 and tloop < 480:
                elist.append(e1_1(xcenter, -30, 'blue', 0, 5, 40, 40, '1e1', tloop))
                
            if tloop % random.randint(20, 25) == 0 and 960 > tloop > 480:
                elist.append(e1_1(xcenter, -30, 'blue', 0, 5, 40, 40, '1e1', tloop))
                
            if tloop% random.randint(40, 60) == 0 and 1500 > tloop > 960:
                elist.append(e1_1b(xposenemy, -30, 'brown',0, 5, 40, 40, '1e1b', tloop))
                
            if tloop% random.randint(30, 60) == 0 and 2100 > tloop > 1060:
                elist.append(e1_2(xposenemy, -30, 'brown',0, 5, 40, 40, '1e2', tloop))
                
            if tloop% random.randint(20, 60) == 0 and 2100 > tloop > 1060:
                elist.append(e1_2b(xposenemy, -30, 'brown',0, 5, 40, 40, '1e2b', tloop))
                
            if tloop% random.randint(20, 60) == 0 and 2100 > tloop > 1200:
                elist.append(e1_1(xposenemy, -30, 'blue',0, 5, 40, 40, '1e1', tloop))
                
            if tloop% random.randint(10, 20) == 0 and 2000 > tloop > 1600:
                elist.append(e1_4b1(0, ytop, 'brown',random.randint (3, 7), 0, 36, 32, '1e4b-1', tloop))
                
            if tloop% random.randint(10, 20) == 0 and 2000 > tloop > 1600:
                elist.append(e1_4b2(450, ytop, 'brown',random.randint(-7, -3), 0, 36, 32, '1e4b-2', tloop))
                
                
            if tloop == 2160:
                elist.append(e1_3(185, 100, 'blue',0, 0, 60, 72, '1e3', tloop))
                
            if tloop == 2360:
                elist.append(e1_3(85, 150, 'blue',0, 0, 60, 72, '1e3', tloop))
                elist.append(e1_3(285, 150, 'blue',0, 0, 60, 72, '1e3', tloop))
                
            if tloop % 24 == 0 and 2900 > tloop > 2700:
                elist.append(e1_7(0, 600, 'blue', 0, -6, 41, 41, '1e7-1', tloop))
                
                elist.append(e1_7(410, 600, 'blue', 0, -6, 41, 41, '1e7-2', tloop))                
                
            if tloop% random.randint(5, 10) == 0 and 2600 > tloop > 2200:
                elist.append(e1_5(xposenemy, -30, 'blue',random.randint(-2, 2), random.randint(10, 15), 36, 32, '1e5', tloop))
                
            if tloop% random.randint(5, 10) == 0 and 2600 > tloop > 2200:
                elist.append(e1_5b(xposenemy, -30, 'brown',random.randint(-2, 2), random.randint(10, 15), 36, 32, '1e5b', tloop))
                
            if 2848 > tloop > 2600 and tloop % 33 == 0:
                elist.append(e1_6b(xcenter, -30, 'brown', 0, 5, 36, 32, '1e6b', tloop))
                
            if tloop == 3000:
                elist.append(e1_8(175, 150, 'blue',0, 1, 82, 65, '1e8', tloop))
                
            if tloop == 3360:
                elist.append(e1_3(55, 150, 'blue',0, 0, 60, 72, '1e3', tloop))
                elist.append(e1_3(125, 150, 'blue',0, 0, 60, 72, '1e3', tloop))
                elist.append(e1_3(195, 150, 'blue',0, 0, 60, 72, '1e3', tloop))
                elist.append(e1_3(265, 150, 'blue',0, 0, 60, 72, '1e3', tloop))
                elist.append(e1_3(335, 150, 'blue',0, 0, 60, 72, '1e3', tloop))
                
            if tloop% random.randint(10, 20) == 0 and 4000 > tloop > 3400:
                elist.append(e1_4b1(0, ytop, 'brown',random.randint (3, 7), 0, 36, 32, '1e4b-1', tloop))
                
            if tloop% random.randint(10, 20) == 0 and 4000 > tloop > 3400:
                elist.append(e1_4b2(450, ytop, 'brown',random.randint(-7, -3), 0, 36, 32, '1e4b-2', tloop))
                
            if tloop%80-(random.randint(0, 79)) == 0 and 4000>  tloop > 3200:
                elist.append(e1_2(xposenemy, -30, 'blue',0, 5, 24, 48, '1e2', tloop))
                
            if tloop%80-(random.randint(0, 79)) == 0 and 4000 >tloop > 3600:
                elist.append(e1_2b(xposenemy, -30, 'brown',0, 5, 24, 48, '1e2b', tloop))
                
            if tloop == 4100:
                bossl.append(boss1(135, 75, 'non', 0, 0, 234, 124, 'boss1', tloop))
                
                bossalive=True
                mode = 'boss1'
                
            if tloop%5==0:
                player.shoot=True
            
            if tloop%10==0:
                slist.insert(0, [random.randint(0, 450), 0, random.randint(5, 10)])
            ##These are lists that store the information about the instances inside then, the for loops contain conditions for each instance
            if slist!=[]: #List for stars in the background
                for r in slist:
                    r[1]+=r[2]
                    screen.blit(star, (r[0], r[1]))
                    if r[1] > 600:
                        slist.remove(r) #Removes the star if it goes off screen
                        
            if belist!=[]: #List for the enemy bullets
                for s in belist:
                    screen.blit(s.img, (s.xpos, s.ypos)) #Blits the bullet at its position
                    s.xpos += s.xvelo #Every frame, the bullet moves by its defined x and y velocity
                    s.ypos += s.yvelo
                    
                    if player.pos[0]+5 < s.xpos+8 < player.pos[0]+27 and player.pos[1]+7 < s.ypos+ 12< player.pos[1]+ 29:
                        if s.polarity==player.polarity: #If the bullet's color is the same as the player's, the player is unharmed
                            player.points+=100
                            belist.remove(s)
                            
                        elif s.polarity!=player.polarity: #If it isn't, the player suffers damage
                            belist.remove(s)
                            player.hit()
                        
                    
                    if s.ypos>600:
                        belist.remove(s)
                        
            for b in exlist: #Blits the enemy explosions
                screen.blit(exb1, (b[0]-35, b[1]-30))
                if tloop - b[2] <= 15:
                    
                    exb1 = pygame.image.load('exb1_'+str(tloop-b[2])+'.png')
                
                if tloop - b[2] == 16:
                    
                    b[2] = 0
                    
                    exlist.remove(b)
                    
            for c in exlist2:
                screen.blit(exb2, (c[0]-35, c[1]-30))
                if tloop - c[2] <= 15:
                    
                    exb2 = pygame.image.load('exb2_'+str(tloop-c[2])+'.png')
                
                if tloop - c[2] == 16:
                    
                    c[2] = 0
                    
                    exlist2.remove(c)
                
            for p in bossl: #Boss conditions, includes firing patterns
                screen.blit(p.img, (p.xpos, p.ypos))
                if p.health > 0: #This is the health bar for the boss
                    rect2((0, 255, 0), 10, 60, (float(p.health) / float(3000))*300, 10)
                p.xpos += p.xvelo
                p.ypos += p.yvelo
                if p.ypos<player.pos[1]+20<p.ypos+p.sw and p.xpos < player.pos[0]+16 < p.xpos + p.sw and player.cd == 0:
                    player.hit()
                    player.cd +=48
                    
                if p.n == 'boss1':
                    if 0 < ((tloop - p.t) % 960) < 480:
                        if (tloop - p.t) % 66 == 0:
                            belist.insert(0, b4(p.xpos+111, p.ypos, 'blue', aimx(player.pos[0], p.xpos+111, player.pos[1], p.ypos, 4), aimy(player.pos[0], p.xpos+111, player.pos[1], p.ypos, 4)))
                        
                            belist.insert(0, b4(p.xpos+111, p.ypos, 'blue', aimx(player.pos[0], p.xpos+111, player.pos[1], p.ypos, 3.5)-(aimy(player.pos[0], p.xpos+111, player.pos[1], p.ypos, 3.5)/7), aimy(player.pos[0], p.xpos+111, player.pos[1], p.ypos, 3.5)+(aimx(player.pos[0], p.xpos+111, player.pos[1], p.ypos, 3.5)/7)))
                        
                            belist.insert(0, b4(p.xpos+111, p.ypos, 'blue', aimx(player.pos[0], p.xpos+111, player.pos[1], p.ypos, 3.5)+(aimy(player.pos[0], p.xpos+111, player.pos[1], p.ypos, 3.5)/7), aimy(player.pos[0], p.xpos+111, player.pos[1], p.ypos, 3.5)-(aimx(player.pos[0], p.xpos+111, player.pos[1], p.ypos, 3.5)/7)))
                            belist.insert(0, b4(p.xpos+111, p.ypos, 'blue', aimx(player.pos[0], p.xpos+111, player.pos[1], p.ypos, 3)-(aimy(player.pos[0], p.xpos+111, player.pos[1], p.ypos, 3)/3), aimy(player.pos[0], p.xpos+111, player.pos[1], p.ypos, 3)+(aimx(player.pos[0], p.xpos+111, player.pos[1], p.ypos, 3)/3)))
                        
                            belist.insert(0, b4(p.xpos+111, p.ypos, 'blue', aimx(player.pos[0], p.xpos+111, player.pos[1], p.ypos, 2)+(aimy(player.pos[0], p.xpos+111, player.pos[1], p.ypos, 3)/3), aimy(player.pos[0], p.xpos+111, player.pos[1], p.ypos, 3)-(aimx(player.pos[0], p.xpos+111, player.pos[1], p.ypos, 3)/3)))
                    
                        if (tloop - p.t) % 36 == 0 or (tloop - p.t) % 48 == 3 or (tloop - p.t) % 48 == 6 or (tloop - p.t) % 48 == 9 or (tloop - p.t) % 48 == 12:
                            belist.insert(0, b3b(p.xpos, p.ypos+50, 'brown', aimx(player.pos[0], p.xpos, player.pos[1], p.ypos+50, 6), aimy(player.pos[0], p.xpos, player.pos[1], p.ypos+50, 6)))
                            
                            belist.insert(0, b3b(p.xpos+222, p.ypos+50, 'brown', aimx(player.pos[0], p.xpos+222, player.pos[1], p.ypos+50, 6), aimy(player.pos[0], p.xpos+222, player.pos[1], p.ypos+50, 6)))
                            
                    if 481 < ((tloop - p.t) % 960) < 959:
                        
                        if (tloop - p.t) % (random.randint(5, 15)) == 0:
                            belist.insert(0, b1(xposenemy, p.ypos, 'blue', 0, random.randint(5, 15)))
                            
                            belist.insert(0, b1b(xposenemy, p.ypos, 'brown', 0, random.randint(5, 15)))
                        
                for w in blist:
                    if p.ypos < w[1] < p.ypos + p.sw and p.xpos < w[0] < p.xpos + p.sl:
                        p.hit()
                        blist.remove(w)
                        
                if p.alive==False:
                    bossalive = False
                    
                
                    
            for q in elist: #Enemy behavior and algorithms... Note that the enemy shooting algorithm is hardcoded, to make it scripted
                screen.blit(q.img, (q.xpos, q.ypos))
                q.xpos += q.xvelo
                q.ypos += q.yvelo
                if q.ypos>630 or q.ypos < -30:
                    q.alive='NOT'

                if q.xpos > 480 or q.xpos < -30:
                    q.alive='NOT'                
                if q.n == '1e1':
                    if tloop == q.t +12:
                        q.xvelo = (random.randint (-2, 2))/2
                        
                if q.n=='1e1b':
                    if tloop == q.t +12:
                        q.xvelo = (random.randint (-2, 2))/2
                        
                        
                if q.n=='1e2': #Blocks of code identifying what enemies will shoot and the behavior of their bullets
                    if tloop%40==random.randint(0, 39):
                        belist.insert(0, b1(q.xpos+8, q.ypos, 'blue', 0, 10))
                        
                if q.n=='1e2b':
                    if tloop%40==random.randint(0, 39):
                        belist.insert(0, b1b(q.xpos+8, q.ypos, 'brown', 0, 10))
                        
                if q.n=='1e3':
                    if (tloop-q.t)%40==0:
                        belist.insert(0, b1(q.xpos+8, q.ypos, 'blue', 0, 10))
                        belist.insert(0, b1(q.xpos+8, q.ypos, 'blue', 1, 9.5))
                        belist.insert(0, b1(q.xpos+8, q.ypos, 'blue', -1, 9.5))
                        belist.insert(0, b1(q.xpos+8, q.ypos, 'blue', 2, 9))
                        belist.insert(0, b1(q.xpos+8, q.ypos, 'blue', -2, 9))
                        
                    if (tloop - q.t) == 96:
                        q.yvelo = 2
                        
                if q.n == '1e4b-1':
                    if (tloop - q.t) % 48==0:
                        belist.insert(0, b2b(q.xpos+12, q.ypos+20, 'brown', aimx(player.pos[0], q.xpos, player.pos[1], q.ypos, 5), aimy(player.pos[0], q.xpos, player.pos[1], q.ypos, 5)))
                        
                if q.n == '1e4b-2':
                    if (tloop - q.t) % 48==0:
                        belist.insert(0, b2b(q.xpos+12, q.ypos+20, 'brown', aimx(player.pos[0], q.xpos, player.pos[1], q.ypos, 5), aimy(player.pos[0], q.xpos, player.pos[1], q.ypos, 5)))
                        
                if q.n=='1e6b':
                    if (tloop-q.t)%30==0:
                        belist.insert(0, b3b(q.xpos+8, q.ypos, 'brown', 0.5, 12))
                        belist.insert(0, b3b(q.xpos+8, q.ypos, 'blue', 1.5, 9.5))
                        belist.insert(0, b3b(q.xpos+8, q.ypos, 'blue', 3, 8))
                        belist.insert(0, b3b(q.xpos+8, q.ypos, 'blue', 5, 6))
                        belist.insert(0, b3b(q.xpos+8, q.ypos, 'blue', 7, 4))

                    if (tloop-q.t)%30==15:
                        belist.insert(0, b3b(q.xpos+8, q.ypos, 'brown', -0.5, 12))
                        belist.insert(0, b3b(q.xpos+8, q.ypos, 'blue', -1.5, 9.5))
                        belist.insert(0, b3b(q.xpos+8, q.ypos, 'blue', -3, 8))
                        belist.insert(0, b3b(q.xpos+8, q.ypos, 'blue', -5, 6))
                        belist.insert(0, b3b(q.xpos+8, q.ypos, 'blue', -7, 4))

                if q.n == '1e7-1' or q.n == '1e7-2':
                    
                    if q.n == '1e7-1':
                        if tloop - q.t > 32:
                            q.xvelo = 1.5
                    if q.n == '1e7-2':
                        if tloop - q.t > 32:
                            q.xvelo = -1.5
                            
                    if (tloop - q.t) % 60 == 0:
                        belist.insert(0, b4(q.xpos+8, q.ypos, 'blue', aimx(player.pos[0], q.xpos, player.pos[1], q.ypos, 2), aimy(player.pos[0], q.xpos, player.pos[1], q.ypos, 2)))
                        
                        belist.insert(0, b4(q.xpos+8, q.ypos, 'blue', aimx(player.pos[0], q.xpos, player.pos[1], q.ypos, 1.5)-(aimy(player.pos[0], q.xpos, player.pos[1], q.ypos, 1.5)/2), aimy(player.pos[0], q.xpos, player.pos[1], q.ypos, 1.5)+(aimx(player.pos[0], q.xpos, player.pos[1], q.ypos, 1.5)/2)))
                        
                        belist.insert(0, b4(q.xpos+8, q.ypos, 'blue', aimx(player.pos[0], q.xpos, player.pos[1], q.ypos, 1.5)+(aimy(player.pos[0], q.xpos, player.pos[1], q.ypos, 1.5)/2), aimy(player.pos[0], q.xpos, player.pos[1], q.ypos, 1.5)-(aimx(player.pos[0], q.xpos, player.pos[1], q.ypos, 1.5)/2)))
                        
                if q.n == '1e8':
                    if tloop - q.t >= 48 and (tloop - q.t) % 48 == 0:
                        belist.insert(0, b3(q.xpos+40, q.ypos+32, 'blue', 0, 8))
                        belist.insert(0, b3(q.xpos+40, q.ypos+32, 'blue', float(64/5)**0.5, float(256/5)**0.5))
                        belist.insert(0, b3(q.xpos+40, q.ypos+32, 'blue', float(32**0.5), float(32**0.5)))
                        belist.insert(0, b3(q.xpos+40, q.ypos+32, 'blue', float(256/5)**0.5, float(64/5)**0.5))
                        belist.insert(0, b3(q.xpos+40, q.ypos+32, 'blue', 8, 0))
                        belist.insert(0, b3(q.xpos+40, q.ypos+32, 'blue', float(64/5)**0.5, -float(256/5)**0.5))
                        belist.insert(0, b3(q.xpos+40, q.ypos+32, 'blue', float(32**0.5), -float(32**0.5)))
                        belist.insert(0, b3(q.xpos+40, q.ypos+32, 'blue', float(256/5)**0.5, -float(64/5)**0.5))
                        belist.insert(0, b3(q.xpos+40, q.ypos+32, 'blue', 0, -8))
                        belist.insert(0, b3(q.xpos+40, q.ypos+32, 'blue', -float(64/5)**0.5, -float(256/5)**0.5))
                        belist.insert(0, b3(q.xpos+40, q.ypos+32, 'blue', -float(32**0.5), -float(32**0.5)))
                        belist.insert(0, b3(q.xpos+40, q.ypos+32, 'blue', -float(256/5)**0.5, -float(64/5)**0.5))
                        belist.insert(0, b3(q.xpos+40, q.ypos+32, 'blue', -8, 0))
                        belist.insert(0, b3(q.xpos+40, q.ypos+32, 'blue', -float(64/5)**0.5, float(256/5)**0.5))
                        belist.insert(0, b3(q.xpos+40, q.ypos+32, 'blue', -float(32**0.5), float(32**0.5)))
                        belist.insert(0, b3(q.xpos+40, q.ypos+32, 'blue', -float(256/5)**0.5, float(64/5)**0.5))
                        
                if q.ypos<player.pos[1]+20<q.ypos+q.sw and q.xpos < player.pos[0]+16 < q.xpos + q.sl and player.cd == 0:
                    player.hit()
                    player.cd +=48
                    q.alive='NOT'
                    
                if q.alive == False:
                    player.points +=100
                    q.alive='NOT'
                    if q.polarity == 'blue':
                        exlist.append([q.xpos, q.ypos, tloop, exb1])
                        
                    if q.polarity == 'brown':
                        exlist2.append([q.xpos, q.ypos, tloop, exb2])
                    
                if q.alive == 'NOT':
                    elist.remove(q)
            
            if blist!=[]: #This list is for the bullets fired by the player
                for s in blist:
                    if s[2]=='blue' and s[3]=='l':
                        screen.blit(lbullet, (s[0], s[1]))
                    elif s[2]=='brown' and s[3]=='l':
                        screen.blit(lbullet2, (s[0], s[1]))
                        
                    elif s[2]=='blue' and s[3]=='r':
                        screen.blit(rbullet, (s[0], s[1]))
                        
                    elif s[2]=='brown' and s[3]=='r':
                        screen.blit(rbullet2, (s[0], s[1]))
                        
                    s[1]-=10
                    if s[1]<0:
                        blist.remove(s)
                        
            for q in elist: #collision against enemy (bullet)
                for w in blist:
                    if q.ypos < w[1] < q.ypos + 40 and q.xpos < w[0] < q.xpos + 40 and w[2]!=q.polarity:#enemy hitbox
                        q.hit2()
                        blist.remove(w)
                    elif q.ypos < w[1] < q.ypos + 40 and q.xpos < w[0] < q.xpos + 40 and w[2]==q.polarity:
                        blist.remove(w)
                        q.hit()
             
            ##Below is the stopping algorithm for the player itself
            if player.pos[0]<0:
                player.pos[0]+=1
                player.move[0]=0
                
            if player.pos[0]>425:
                player.pos[0]-=1
                player.move[0]=0
                
            if player.pos[1]<0:
                player.pos[1]+=1
                player.move[1]=0
                
            if player.pos[1]>570:
                player.pos[1]-=1
                player.move[1]=0
                
            blit (theship, player.pos[0], player.pos[1])
            
            ##Blits the score, lives and health of the player
            text('Score:',myfont, "green", 0, 13)
            text(str(player.points),myfont, "green", 100, 13)
            
            text('Lives:',myfont, "red", 0, 36)
            text(str(player.lives),myfont, "red", 100, 36)
            
            rect2((0, 0, 88), 268, 13, 181, 24)
            rect2((0, 0, 0), 271, 16, 175, 18)
            rect2((0, 50, 255), 271, 16, (35*player.health), 18)
            text('Health',myfont, "aquamarine", 275, 13)
            
            flip()
            
            events=pygame.event.get()
            for f in events:
                if f.type == KEYDOWN:
                    if key[pygame.K_z] and player.shoot==True:
                        x=player.pos[0]
                        bpos[0]=x
                        y=player.pos[1]
                        bpos[1]=y
                        
                        x2=player.pos[0]+20
                        y2=player.pos[1]
                        
                        blist.insert(0, [x,y,player.polarity, 'l'])
                        blist.insert(0, [x2, y2, player.polarity, 'r'])
                        player.shoot=False
            for e in events: 
                if e.type == QUIT:
                    running=False   # Stop the program, it's detected quit...
            
                if e.type == KEYDOWN: #All keyboards, these are key commands for the player
                    if key[pygame.K_RIGHT]:
                        player.pos[0] +=player.move[0]
                        player.move[0]=4
                    if key[pygame.K_LEFT]:
                        player.pos[0] -=player.move[0]
                        player.move[0]=4
                    if key[pygame.K_UP]:
                        player.pos[1] -=player.move[1]
                        player.move[1]=4
                    if key[pygame.K_DOWN]:
                        player.pos[1] +=player.move[1]
                        player.move[1]=4
                    if key[pygame.K_SPACE] and player.polarity == 'blue':
                        player.polarity = 'brown'
                    elif key[pygame.K_SPACE] and player.polarity == 'brown':
                        player.polarity = 'blue'
                    
                    if key[pygame.K_k]:
                        player.hit()
                if e.type == KEYDOWN and e.key == pygame.K_p:
                    blit(pause, 0, 0)
                    text2('Paused',titlefont,(255, 160, 0), 70, 50)
                        
                    text2('press r to return',selfont,(0, 255, 55), 85, 200)                   
                    text2('press q to quit',selfont,(255, 75, 0), 85, 250)
                    
                    text2('press m to return to menu',myfont,(0, 255, 55), 85, 300)
                    while 1:
                        
                        e = pygame.event.wait()
                        flip()
                        if e.type == QUIT:
                            running=False   # Stop the program, it's detected quit...
                        if e.type == KEYDOWN and e.key == pygame.K_r:
                            break
                        
                        elif e.type == KEYDOWN and e.key == pygame.K_q:
                            sys.exit()
                            
                        elif e.type == KEYDOWN and e.key == pygame.K_m:
                            mode = 'start'
                            break
                        
            tloop+=1 #Every frame, the counter for the frames elapsed goes up by 1
            if player.cd > 0:
                
                player.cd-=1
                
            clock.tick(48)
        if mode=='over' or mode == 'win':
            blit(over, 0, 0)
            pygame.key.set_repeat(5, 6)
            rect3((0, 0, 0), 20, 560, 70, 590)
            rect3((255, 25, 0), 22, 562, 68, 588)
            text2('Back', selfont2, (0, 0, 64), 25, 565)
            
            rect3((0, 0, 0), 102, 392, 318, 463)
            rect3((0, 255, 50), 110, 400, 310, 455)
            text2('Save score', selfont, (0, 0, 64), 110, 410)
            
            if 20 < mpos[0] < 70 and 560 < mpos[1] < 590 and butt ==(1, 0, 0):
                mode = 'start'
                player.lives=5
                player.health=5
                player.points=0
                blist=[]
                elist=[]
                slist=[]
                belist=[]
                exlist=[]
                exlist2=[]
                bossl=[]
                b=0
                c=0
                player.pos=[225, 450]
                player.polarity='blue'
                tloop=0
                bossalive = False
            if mode =='over':
                text('game over',selfont, "red", 140, 150)
            if mode == 'win':
                text('YOU WIN',selfont, "aquamarine", 140, 150)
            text('score:',selfont, "green", 140, 186)
            text(str(player.points),selfont, "green", 250, 186)
            text(stname.join(name),selfont, "green", 120, 286)
            
            events=pygame.event.get()
            for e in events: 
                if e.type == KEYDOWN:
                    whatkey=pygame.key.name(e.key)
                    
                    if whatkey=='backspace' and len(name)>=1:
                        name.pop(-1)
                    if whatkey=='space':
                        name.append(' ')
                    if len(name)>=15:
                        name.pop(-1)
                    if whatkey!='backspace' and whatkey!='return' and whatkey!='space':
                        name.append(whatkey)
                if e.type == QUIT:
                    running=False   # Stop the program, it's detected quit...
            if 102 < mpos[0] < 318 and 392 < mpos[1] < 463 and butt ==(1, 0, 0) and sc == 0:
                nlist.append(stname.join(name))
                sclist.append(player.points)
                sc+=1
                while True:
                    pull=sclist[0]
                    pull2=nlist[0]
                    if sclist2==[]:
                        sclist2.append(pull)
                        nlist2.append(pull2)
                        sclist.pop(0)
                        nlist.pop(0)
                        if sclist==[]:
                            break
                        else:
                            continue
                    if pull <= sclist2[sor]:
                        sor+=1
                    elif pull>sclist2[sor]:
                        sclist2.insert(sor, pull)
                        nlist2.insert(sor, pull2)
                        sclist.pop(0)
                        nlist.pop(0)
                        sor=0
                    if sor==len(sclist2):
                        sclist2.append(pull)
                        nlist2.append(pull2)
                        sclist.pop(0)
                        nlist.pop(0)
                        sor=0
                    if sclist==[]:
                        break
                ff=open('highscores.txt','w')
                while fc<len(sclist2) and fc < 10:
                    ff.write(str(nlist2[fc])+'\t'+str(sclist2[fc])+'\n')
                    fc+=1
                ff.close()
                fil.close()
            flip()
                    
                
finally:
    pygame.quit()  # Keep this IDLE friendly 
