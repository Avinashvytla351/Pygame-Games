import pygame
import random
import winsound
class block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface([20,40])
        self.image.fill((155,102,255))
        self.rect=self.image.get_rect()
        self.rect.center=(40,50)
    def update(self,flag):
        if flag!=290:
            self.rect.y=290-flag
        else:
            self.rect.y=290
class obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        x=random.choice([20,30,35])
        y=random.choice([20,30,35])
        self.image = pygame.Surface([x,y])
        self.image.fill((0,200,0))
        self.rect = self.image.get_rect()
        self.rect.center=(490,330)
    v2=0
    def update(self,os):
        if self.v2==0:
            x=random.choice([20,30,35])
            y=random.choice([20,30,35])
            self.image = pygame.Surface([x,y])
            self.image.fill((0,200,0))
            self.rect = self.image.get_rect()
            self.rect.center=(490,330)
            self.v2=1
        self.rect.x-=os
        if self.rect.x<0:
            i=random.choice([1,0])
            if i==0:
                x=random.choice([20,30,35])
                y=random.choice([20,30,35])
                self.image = pygame.Surface([x,y])
                self.image.fill((0,200,0))
                self.rect = self.image.get_rect()
                self.rect.center=(490,330)
            if i==1:
                x=10
                y=10
                self.image = pygame.Surface([x,y])
                self.image.fill((0,200,0))
                self.rect = self.image.get_rect()
                self.rect.center=(490,290)
pygame.init()
scr = pygame.display.set_mode([500,350])
pygame.display.set_caption("Game")
font_name=pygame.font.match_font('arial')
def draw_text(surf,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,((0,0,0)))
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surf.blit(text_surface,text_rect)
s= pygame.sprite.Group()
q= pygame.sprite.Group()
p=block()
s.add(p)
o=obstacles()
q.add(o)
c=pygame.time.Clock()
sc=0
go=0
v=0
x=0
speed=60
count=0
flag=0
flag1=0
m=2
ve=11
f=290
dis=0
tem=0
le=0
leg=0
dc=0
sco=0
os=3
osc=0
r=True
t=False
t1=False
while r:
    if go==0:
        scr.fill((250,250,200))
        draw_text(scr,str(sco),50,250,100)
        draw_text(scr,"score",25,250,150)
        draw_text(scr,"Press spacebar to start",20,250,185)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            go=1
            sc=0
            v=0
            sco=0
            os=3
            osc=0
    c.tick(speed)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            r=False
    if go==1:
        scr.fill((250,250,200))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and flag==0:
            flag=1
            t=True
        if keys[pygame.K_DOWN]:
            t1=True
        if t1:
            f=-20
            pygame.draw.rect(scr, (155,102,255),(40,310,20,20))
            s.update(f)
            s.draw(scr)
        if t:
            if dis==0:
                tem=0
            if tem==0:
                dis+=3
            if dis==75:
                tem=1
            if tem==1:
                dis-=5
                if dis==0:
                    t=False
            s.update(dis)
            s.draw(scr)
        else:
            s.update(f)
            s.draw(scr)
            f=290
        z=pygame.sprite.spritecollide(p,q,False)
        if len(z)!=0:
            v=v+1
        sc=sc+1
        count+=1
        if v>5:
            go=0
        if keys[pygame.K_UP]==0:
            flag=0
            f=290
        if keys[pygame.K_DOWN]==0:
            t1=False
        sco=sc//10
        if sco!=osc and sco%100==0 and os<8:
            os=os+1
        if sco!=osc and sco%100==0:
            winsound.Beep(1000,250)
            winsound.Beep(1000,250)
            osc=sco
        draw_text(scr,str(sco),45,250,10)
        draw_text(scr,"score",20,250,50)
        if t==False:
            if le==0:
                pygame.draw.rect(scr,(250,250,250),(35,320,10,20))
            if le==1:
                pygame.draw.rect(scr,(250,250,250),(35,310,10,20))
            if le==0:
                leg+=1
            if leg==5:
                le=1
            if le==1:
                leg-=1
            if leg==0:
                le=0
        q.update(os)
        q.draw(scr)
    pygame.draw.rect(scr,(100,0,0),(0,340,500,15))
    pygame.display.update()
pygame.quit()
