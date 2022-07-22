import pygame
import random
class Block(pygame.sprite.Sprite):
    def __init__(self,i):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill((200,0,0))
        self.rect = self.image.get_rect()
        x=random.randint(1,450)
        self.rect.center=(x,10)
        self.s=5
        self.sc=i
    def update(self):
        self.rect.y=self.s
        self.s+=15
        if(self.s>460):
            self.s=5
            x=random.randint(1,450)
            self.rect.center=(x,10)
class mouse1(pygame.sprite.Sprite):
    def update(self,size):
        super().update()
        k=pygame.mouse.get_pos()
        self.image=pygame.Surface([size,10])
        self.image.fill((255,25,255))
        self.rect=self.image.get_rect()
        self.rect.center=(k[0],440)
pygame.init()
scr = pygame.display.set_mode([500,500])
pygame.display.set_caption("Game")
s= pygame.sprite.Group()
r=True
c=pygame.time.Clock()
bs=pygame.sprite.Group()
player = Block(0)
bs.add(player)
he=pygame.sprite.Group()
def lif(v):
    for i in range(0,v,1):
        pygame.draw.rect(scr,(255,255,0),(i*10,20,10,10))
size=20
p=mouse1()
s.add(p)
font_name=pygame.font.match_font('arial')
def draw_text(surf,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,((0,0,0)))
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surf.blit(text_surface,text_rect)
sc=0
v=0
r2=200
q=20
sa=0
go=False
    
while(r):
    if go:
       scr.fill((255,255,255))
       draw_text(scr,str(sc),60,250,200)
       draw_text(scr,"score",30,250,250)
       draw_text(scr,"Click anywhere to RESTART",18,250,290)
       t=pygame.mouse.get_pressed()
       if t[0]==1:
           q=20
           sc=0
           sa=0
           v=0
           size=20
           go=False
       pygame.display.update()
    c.tick(random.randint(45,55))
    scr.fill((r2,r2,r2))
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            r=False
    if go==False:
        s.update(size)
        lif(q)
        z=pygame.sprite.spritecollide(p,bs,False)
        v=v+1
        if z:
            sc+=1
            if(size<70):
                size+=10
            v=0
        else:
            if size>20 and v>30:
                size=20
                v=0
            if v>30:
                q=q-1
                sa=sa+10
                v=0
        if q<=0:
            go=True
        s.draw(scr)
        bs.draw(scr)
        he.draw(scr)
        draw_text(scr,str(sc),45,250,10)
        draw_text(scr,"score",20,250,50)
        draw_text(scr,"Life",15,210-sa,15)
        bs.update()
        pygame.display.update()
        scr.fill((0,0,0))
pygame.quit()
            
