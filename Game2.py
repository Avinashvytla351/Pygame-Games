import pygame
import random
pygame.init()
scr=pygame.display.set_mode([500,500])
c=pygame.time.Clock()
cl=150
cp=random.choice([0,349])
s=150
l=175
x=0
todo=0
go=True
sc=0
font_name=pygame.font.match_font('arial')
def draw_text(surf,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,((0,0,0)))
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surf.blit(text_surface,text_rect)
def slide(cl,cp):
    pygame.draw.rect(scr,(200,0,0),(cp,440,cl,20))
r=True
while r:
    if go==False:
       scr.fill((255,255,255))
       draw_text(scr,str(sc-1),60,250,200)
       draw_text(scr,"score",30,250,250)
       draw_text(scr,"Right_Click anywhere to RESTART",18,250,290)
       pygame.display.update()
       t=pygame.mouse.get_pressed()
       if t[2]==1:
           cl=150
           cp=random.choice([0,349])
           s=150
           l=175
           x=0
           todo=0
           go=True
           sc=0
    c.tick(100)
    scr.fill((200,200,200))
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            r=False
    if go:
        if cp==0:
            co=0
        if cp==349:
            co=1
        t=pygame.mouse.get_pressed()
        if x==0 and t[0]==1:
            sc=sc+1
            tem=abs(l-cp)
            if cl>20 and tem>4:
                todo=1
            elif cl<20:
                todo=1
            else:
                todo=0
            if todo==1:
                cl=cl-tem
                s=s-tem
            cp=random.choice([0,349])
            if cp==0:
                co=0
            if cp==349:
                co=1
            x=1
        if cl<=0:
            go=False
        if t[0]==0:
            x=0
            todo=0
        slide(cl,cp)
        if co==0:
            cp=cp+1
        elif co==1:
            cp=cp-1
        draw_text(scr,str(sc),45,250,10)
        draw_text(scr,"score",20,250,50)
        pygame.draw.rect(scr,(0,0,0),(l,460,s,20))
        pygame.display.update()
pygame.quit()
    
