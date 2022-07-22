import pygame
pygame.init()
scr=pygame.display.set_mode((500,545))
c=pygame.time.Clock()
l={}
for i in range(15):
    l[i]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def block(x,y):
    pygame.draw.rect(scr,(255,150,0),(x,y,30,30))
    pygame.draw.rect(scr,(255,200,0),(x,y,23,23))
def move(i,y,n):
    for k in range(0,n):
        block(3+((k+i)*33),470-(y*33))
font_name=pygame.font.match_font('comicsansms')
def draw_text(surf,text,size,x,y,c):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,(c))
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surf.blit(text_surface,text_rect)
r=True
i=0
it=0
n=6
f=0
y=0
ny=0
nt=0
go=0
sc=0
sp=10
ot=0
vo=0
to=1
while r:
    scr.fill((16,78,139))
    c.tick(sp)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = False
    if go==0:
        draw_text(scr,str(sc),55,250,200,(255,255,255))
        draw_text(scr,"Click anywhere to START",20,250,265,(255,255,255))
        k1=pygame.mouse.get_pressed()
        if k1[0]==1:
            sc=0
            i=0
            it=0
            n=6
            f=0
            y=0
            ny=0
            nt=0
            go=1
            sp=10
            gt=0
            for z in range(15):
                l[z]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if go==1:
        move(int(i),y,n)
        if i+n-1<15 and it==0:
            i=i+1/2
        if i+n-1==15:
            it=1
        if it==1:
            i=i-1/2
        if i==0:
            it=0
        k=pygame.key.get_pressed()
        if k[pygame.K_SPACE]==1 and f==0 and gt!=0 :
            vo=0
            i=int(i)
            ny=y
            nt=1
            for z in range(i,i+n):
                l[y][z]=1
            i=0
            it=0
            y=y+1
            sc=sc+1
            f=1
        if k[pygame.K_SPACE]==0:
            f=0
        if y>11:
            y=11
            for w in range(12):
                for z in range(15):
                    l[w][z]=l[w+1][z]
        for z in range(15):
            for w in range(15):
                if l[z][w]==1:
                    block(3+(w*33),470-(z*33))
        for z in range(15):
            if ny!=0 and nt==1 and to==1:
                if l[y-1][z]!=l[y-2][z] and l[y-1][z]==1 and l[y-2][z]==0:
                    n=n-1
                else:
                    vo=vo+1
        if to==0 and nt==1:
            vo=0
            to=1
        if nt==1:
            if vo==15:
                ot=ot+1
            else:
                ot=0
        if ot>=5 and nt==1:
            if n<6:
                n=n+1
                to=0
                cto=0
        if n<=0:
            go=0
        draw_text(scr,str(sc),45,250,15,(255,255,255))
        if sc%5==0 and sc!=0 and sp<=30 and nt==1:
            sp=sp+2
        nt=0
        gt=1
    pygame.display.update()
pygame.quit()
