import pygame
import random
pygame.init()
scr=pygame.display.set_mode((550,600))
pygame.display.set_caption('Game')
x=275
y=550
w=15
h=15
cx=0
cy=0
f1=-1
def shapes(x,y,w,h,i):
    if i==1:
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==2:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==3:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==4:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==5:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==6:
        pygame.draw.rect(scr,(255,0,0),(x,y,3*w+2*5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==7:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-2*h-2*5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==8:
        pygame.draw.rect(scr,(255,0,0),(x,y,3*w+2*5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-2*w-2*5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==9:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-2*h-2*5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,3*h+2*5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==10:
        pygame.draw.rect(scr,(255,0,0),(x,y,4*w+3*5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-2*w-2*5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==11:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-3*h-3*5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,3*h+2*5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==12:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==13:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==14:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-5))
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==15:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-5))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==16:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-2*h-2*5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==17:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,3*h+2*5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==18:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-5))
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,3*w+2*5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==19:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-5))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-2*w-2*5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==20:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,-h-5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==21:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==22:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,-h-5))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,-h-5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==23:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-5))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,-h-5))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==24:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-5))
        pygame.draw.rect(scr,(255,0,0),(x-w-6,y+h,w,h+5))
        pygame.draw.rect(scr,(255,0,0),(x+w+5,y+h,w,h+5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==25:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-4,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x+w+5,y-h-5,w,h+5))
        pygame.draw.rect(scr,(255,0,0),(x-w-5,y-h-5,w,h+5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==26:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-4))
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x-w-5,y-h-5,w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x-w-5,y+h+5,w+5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==27:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-4))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,h))
        pygame.draw.rect(scr,(255,0,0),(x+w,y-h-5,w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x+w,y+h+5,w+5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==28:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,h))
        pygame.draw.rect(scr,(255,0,0),(x-w-6,y+h,w,h+5))
        pygame.draw.rect(scr,(255,0,0),(x+w+5,y+h,w,h+5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==29:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-4,h))
        pygame.draw.rect(scr,(255,0,0),(x+w+5,y-h-5,w,h+5))
        pygame.draw.rect(scr,(255,0,0),(x-w-5,y-h-5,w,h+5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==30:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-4))
        pygame.draw.rect(scr,(255,0,0),(x-w-5,y-h-5,w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x-w-5,y+h+5,w+5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==31:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-4))
        pygame.draw.rect(scr,(255,0,0),(x+w,y-h-5,w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x+w,y+h+5,w+5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==32:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,h))
        pygame.draw.rect(scr,(255,0,0),(x+w+5,y+h,w,h+5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==33:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,h))
        pygame.draw.rect(scr,(255,0,0),(x-w-6,y+h,w,h+5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==34:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-4,h))
        pygame.draw.rect(scr,(255,0,0),(x-w-5,y-h-5,w,h+5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==35:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-4,h))
        pygame.draw.rect(scr,(255,0,0),(x+w+5,y-h-5,w,h+5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==36:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-4))
        pygame.draw.rect(scr,(255,0,0),(x-w-5,y+h+5,w+5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==37:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-4))
        pygame.draw.rect(scr,(255,0,0),(x-w-5,y-h-5,w+5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==38:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-4))
        pygame.draw.rect(scr,(255,0,0),(x+w,y+h+5,w+5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==39:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-4))
        pygame.draw.rect(scr,(255,0,0),(x+w,y-h-5,w+5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==40:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,h))
        pygame.draw.rect(scr,(255,0,0),(x-w-6,y+h,w,h+5))
        pygame.draw.rect(scr,(255,0,0),(x+w+5,y-h-5,w,h+5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==41:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-4,h))
        pygame.draw.rect(scr,(255,0,0),(x+w+5,y+h,w,h+5))
        pygame.draw.rect(scr,(255,0,0),(x-w-5,y-h-5,w,h+5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==42:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-4))
        pygame.draw.rect(scr,(255,0,0),(x+w,y-h-5,w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x-w-5,y+h+5,w+5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==43:
        pygame.draw.rect(scr,(255,0,0),(x,y,w,2*h+5))
        pygame.draw.rect(scr,(255,0,0),(x,y,w,-h-4))
        pygame.draw.rect(scr,(255,0,0),(x-w-5,y-h-5,w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x+w,y+h+5,w+5,h))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==44:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x+w+5,y+h,w,h+5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==45:
        pygame.draw.rect(scr,(255,0,0),(x,y,2*w+5,h))
        pygame.draw.rect(scr,(255,0,0),(x+w+5,y-h-5,w,h+5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==46:
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-5,h))
        pygame.draw.rect(scr,(255,0,0),(x-w-6,y+h,w,h+5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
    elif i==47:
        pygame.draw.rect(scr,(255,0,0),(x,y,-w-4,h))
        pygame.draw.rect(scr,(255,0,0),(x-w-5,y-h-5,w,h+5))
        pygame.draw.rect(scr,(255,255,0),(x,y,w,h))
def score(i):
    if i==1:
        return 1
    if i==2:
        return 2
    if i==3:
        return 2
    if i==4:
        return 3
    if i==5:
        return 3
    if i==6:
        return 4
    if i==7:
        return 4
    if i==8:
        return 5
    if i==9:
        return 5
    if i==10:
        return 6
    if i==11:
        return 6
    if i==12:
        return 4
    if i==13:
        return 4
    if i==14: 
        return 4
    if i==15:
        return 4
    if i==16:
        return 5
    if i==17:
        return 5
    if i==18:
        return 5
    if i==19:
        return 5
    if i==20:
        return 4
    if i==21:
        return 5
    if i==22:
        return 6
    if i==23:
        return 6
    if i==24:
        return 6
    if i==25:
        return 6
    if i==26:
        return 6
    if i==27:
        return 6
    if i==28:
        return 5
    if i==29:
        return 5
    if i==30:
        return 5
    if i==31:
        return 5
    if i==32:
        return 4
    if i==33:
        return 4
    if i==34:
        return 4
    if i==35:
        return 4
    if i==36:
        return 4
    if i==37:
        return 4
    if i==38:
        return 4
    if i==39:
        return 4
    if i==40:
        return 5
    if i==41:
        return 5
    if i==42:
        return 5
    if i==43:
        return 5
    if i==44:
        return 3
    if i==45:
        return 3
    if i==46:
        return 3
    if i==47:
        return 3
def grid():
    for x in range(75,465,35):
        pygame.draw.rect(scr,(0,0,0),(x,75,5,385))
    for x in range(70,465,35):
        pygame.draw.rect(scr,(0,0,0),(75,x,390,5))
def stat(i,l):
    global x,y,w,h,t,cx,cy,f1
    tx=cx
    ty=cy
    m=pygame.mouse.get_pressed()
    p=pygame.mouse.get_pos()
    shapes(x,y,w,h,i)
    if m[0]==1 and (p[0]<=290) and (p[1]<565):
        t=1
        f1=0
    if t==1:
        x=p[0]
        y=p[1]
        w=30
        h=30
        cx=(p[1]-70)//35
        cy=(p[0]-75)//35
    if m[0]==0:
        if f1==0:
            f1=1
        x=275
        y=550
        w=15
        h=15
        t=0
        if f1==1 and cx<=10 and cy<=10 and cx>=0 and cy>=0:
            if i==1:
                if l[cx][cy]!=1:
                    l[cx][cy]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==2:
                if l[cx][cy]!=1 and (cy+1)<len(l[cx]) and l[cx][cy+1]!=1:
                    l[cx][cy]=1
                    l[cx][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==3:
                if l[cx][cy]!=1 and (cx+1) in l and l[cx+1][cy]!=1:
                    l[cx][cy]=1
                    l[cx+1][cy]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==4:
                if l[cx][cy]!=1 and (cy+1)<len(l[cx]) and cy-1>=0 and l[cx][cy+1]!=1 and l[cx][cy-1]!=1:
                    l[cx][cy]=1
                    l[cx][cy+1]=1
                    l[cx][cy-1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==5:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and l[cx+1][cy]!=1 and l[cx-1][cy]!=1:
                    l[cx][cy]=1
                    l[cx+1][cy]=1
                    l[cx-1][cy]=1
                    return 0
                else:
                    return -1
                f1=-1
            elif i==6:
                if l[cx][cy]!=1 and cy+1<len(l[cx]) and cy-1>=0 and cy+2<len(l[cx]) and l[cx][cy-1]!=1 and l[cx][cy+1]!=1 and l[cx][cy+2]!=1:
                    l[cx][cy]=1
                    l[cx][cy-1]=1
                    l[cx][cy+1]=1
                    l[cx][cy+2]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==7:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cx-2 in l and l[cx-2][cy]!=1 and l[cx-1][cy]!=1 and l[cx+1][cy]!=1:
                    l[cx][cy]=1
                    l[cx+1][cy]=1
                    l[cx-1][cy]=1
                    l[cx-2][cy]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==8:
                if l[cx][cy]!=1 and cy+1<len(l[cx])and cy+2<len(l[cx]) and cy-1>0 and cy-2>=0 and l[cx][cy-2]!=1 and l[cx][cy-1]!=1 and l[cx][cy+1]!=1 and l[cx][cy+2]!=1:
                    l[cx][cy]=1
                    l[cx][cy-2]=1
                    l[cx][cy-1]=1
                    l[cx][cy+1]=1
                    l[cx][cy+2]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==9:
                if l[cx][cy]!=1 and cx+1 in l and cx+2 in l and cx-1 in l and cx-2 in l and l[cx-2][cy]!=1 and l[cx-1][cy]!=1 and l[cx+1][cy]!=1 and l[cx+2][cy]!=1:
                    l[cx-2][cy]=1
                    l[cx-1][cy]=1
                    l[cx][cy]=1
                    l[cx+1][cy]=1
                    l[cx+2][cy]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==10:
                if l[cx][cy]!=1 and cy+1<len(l[cx])and cy+2<len(l[cx])and cy+3<len(l[cx]) and cy-1>0 and cy-2>=0 and l[cx][cy-2]!=1 and l[cx][cy-1]!=1 and l[cx][cy+1]!=1 and l[cx][cy+2]!=1 and l[cx][cy+3]!=1:
                    l[cx][cy-2]=1
                    l[cx][cy-1]=1
                    l[cx][cy]=1
                    l[cx][cy+1]=1
                    l[cx][cy+2]=1
                    l[cx][cy+3]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==11:
                if l[cx][cy]!=1 and cx-3 in l and cx-2 in l and cx-1 in l and cx+1 in l and cx+2 in l and l[cx-3][cy]!=1 and l[cx-2][cy]!=1 and l[cx-1][cy]!=1 and l[cx+1][cy]!=1 and l[cx+2][cy]!=1:
                    l[cx-3][cy]=1
                    l[cx-2][cy]=1
                    l[cx-1][cy]=1
                    l[cx][cy]=1
                    l[cx+1][cy]=1
                    l[cx+2][cy]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==12:
                if l[cx][cy]!=1 and cx-1 in l and cy-1>=0 and cy+1<len(l[cx]) and l[cx-1][cy]!=1 and l[cx][cy-1]!=1 and l[cx][cy+1]!=1:
                    l[cx][cy]=1
                    l[cx-1][cy]=1
                    l[cx][cy-1]=1
                    l[cx][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==13:
                if l[cx][cy]!=1 and cx+1 in l and cy-1>=0 and cy+1<len(l[cx]) and l[cx+1][cy]!=1 and l[cx][cy-1]!=1 and l[cx][cy+1]!=1:
                    l[cx][cy]=1
                    l[cx+1][cy]=1
                    l[cx][cy-1]=1
                    l[cx][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==14:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy+1<len(l[cx]) and l[cx-1][cy]!=1 and l[cx+1]!=1 and l[cx][cy+1]!=1:
                    l[cx][cy]=1
                    l[cx+1][cy]=1
                    l[cx-1][cy]=1
                    l[cx][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==15:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy-1>=0 and l[cx-1][cy]!=1 and l[cx+1]!=1 and l[cx][cy-1]!=1:
                    l[cx][cy]=1
                    l[cx+1][cy]=1
                    l[cx-1][cy]=1
                    l[cx][cy-1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==16:
                if l[cx][cy]!=1 and cx-1 in l and cx-2 in l and cy-1>=0 and cy+1<len(l[cx]) and l[cx-1][cy]!=1 and l[cx-2][cy]!=1 and l[cx][cy-1]!=1 and l[cx][cy+1]!=1:
                    l[cx][cy]=1
                    l[cx-1][cy]=1
                    l[cx-2][cy]=1
                    l[cx][cy-1]=1
                    l[cx][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==17:
                if l[cx][cy]!=1 and cx+1 in l and cx+2 in l and cy-1>=0 and cy+1<len(l[cx]) and l[cx+1][cy]!=1 and l[cx+2][cy]!=1 and l[cx][cy-1]!=1 and l[cx][cy+1]!=1:
                    l[cx][cy]=1
                    l[cx+1][cy]=1
                    l[cx+2][cy]=1
                    l[cx][cy-1]=1
                    l[cx][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==18:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy+1<len(l[cx]) and cy+2<len(l[cx]) and l[cx-1][cy]!=1 and l[cx+1]!=1 and l[cx][cy+1]!=1 and l[cx][cy+2]!=1:
                    l[cx][cy]=1
                    l[cx+1][cy]=1
                    l[cx-1][cy]=1
                    l[cx][cy+1]=1
                    l[cx][cy+2]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==19:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy-1>=1 and cy-2>=0 and l[cx-1][cy]!=1 and l[cx+1]!=1 and l[cx][cy-1]!=1 and l[cx][cy-2]!=1:
                    l[cx][cy]=1
                    l[cx+1][cy]=1
                    l[cx-1][cy]=1
                    l[cx][cy-1]=1
                    l[cx][cy-2]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==20:
                if l[cx][cy]!=1 and cx-1 in l and cy+1<len(l[cx]) and l[cx-1][cy]!=1 and l[cx-1][cy+1]!=1 and l[cx][cy+1]!=1:
                    l[cx][cy]=1
                    l[cx][cy+1]=1
                    l[cx-1][cy+1]=1
                    l[cx-1][cy]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==21:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy+1<len(l[cx]) and cy-1>=0 and l[cx+1][cy]!=1 and l[cx-1][cy]!=1 and l[cx][cy+1]!=1 and l[cx][cy-1]!=1:
                    l[cx][cy]=1
                    l[cx-1][cy]=1
                    l[cx+1][cy]=1
                    l[cx][cy-1]=1
                    l[cx][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==22:
                if l[cx][cy]!=1 and cx-1 in l and cy-1>=0 and cy+1<len(l[cx]) and l[cx-1][cy-1]!=1 and l[cx-1][cy]!=1 and l[cx-1][cy+1]!=1 and l[cx][cy-1]!=1 and l[cx][cy+1]!=1:
                    l[cx][cy]=1
                    l[cx-1][cy-1]=1
                    l[cx-1][cy]=1
                    l[cx-1][cy+1]=1
                    l[cx][cy-1]=1
                    l[cx][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==23:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy-1>=0 and l[cx-1][cy-1]!=1 and l[cx-1][cy]!=1 and l[cx][cy-1]!=1 and l[cx+1][cy-1]!=1 and l[cx+1][cy]!=1:
                    l[cx][cy]=1
                    l[cx-1][cy-1]=1
                    l[cx-1][cy]=1
                    l[cx][cy-1]=1
                    l[cx+1][cy-1]=1
                    l[cx+1][cy]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==24:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy-1>=0 and cy+1<len(l[cx]) and l[cx+1][cy-1]!=1 and l[cx+1][cy+1]!=1 and l[cx][cy-1]!=1 and l[cx][cy+1]!=1 and l[cx-1][cy]!=1:
                    l[cx][cy]=1
                    l[cx+1][cy-1]=1
                    l[cx+1][cy+1]=1
                    l[cx][cy-1]=1
                    l[cx][cy+1]=1
                    l[cx-1][cy]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==25:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy-1>=0 and cy+1<len(l[cx]) and l[cx-1][cy-1]!=1 and l[cx-1][cy+1]!=1 and l[cx][cy-1]!=1 and l[cx][cy+1]!=1 and l[cx+1][cy]!=1:
                    l[cx][cy]=1
                    l[cx-1][cy-1]=1
                    l[cx-1][cy+1]=1
                    l[cx][cy-1]=1
                    l[cx][cy+1]=1
                    l[cx+1][cy]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==26:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy-1>=0 and cy+1<len(l[cx]) and l[cx+1][cy]!=1 and l[cx-1][cy]!=1 and l[cx-1][cy-1]!=1 and l[cx][cy+1]!=1 and l[cx+1][cy-1]!=1:
                    l[cx][cy]=1
                    l[cx-1][cy-1]=1
                    l[cx+1][cy-1]=1
                    l[cx][cy+1]=1
                    l[cx+1][cy]=1
                    l[cx-1][cy]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==27:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy-1>=0 and cy+1<len(l[cx]) and l[cx-1][cy+1]!=1 and l[cx-1][cy]!=1 and l[cx][cy-1]!=1 and l[cx+1][cy+1]!=1 and l[cx+1][cy]!=1:
                    l[cx][cy]=1
                    l[cx+1][cy+1]=1
                    l[cx+1][cy]=1
                    l[cx][cy-1]=1
                    l[cx-1][cy]=1
                    l[cx-1][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==28:
                if l[cx][cy]!=1 and cx+1 in l and cy-1>=0 and cy+1<len(l[cx]) and l[cx][cy-1]!=1 and l[cx][cy+1]!=1 and l[cx+1][cy-1]!=1 and l[cx+1][cy+1]!=1:
                    l[cx][cy]=1
                    l[cx][cy-1]=1
                    l[cx][cy+1]=1
                    l[cx+1][cy-1]=1
                    l[cx+1][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==29:
                if l[cx][cy]!=1 and cx-1 in l and cy-1>=0 and cy+1<len(l[cx]) and l[cx][cy-1]!=1 and l[cx][cy+1]!=1 and l[cx-1][cy-1]!=1 and l[cx-1][cy+1]!=1:
                    l[cx][cy]=1
                    l[cx][cy-1]=1
                    l[cx][cy+1]=1
                    l[cx-1][cy-1]=1
                    l[cx-1][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==30:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy-1>=0 and l[cx-1][cy-1]!=1 and l[cx-1][cy]!=1 and l[cx+1][cy-1]!=1 and l[cx+1][cy]!=1:
                    l[cx][cy]=1
                    l[cx-1][cy-1]=1
                    l[cx-1][cy]=1
                    l[cx+1][cy-1]=1
                    l[cx+1][cy]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==31:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy+1<len(l[cx]) and l[cx-1][cy]!=1 and l[cx-1][cy+1]!=1 and l[cx+1][cy]!=1 and l[cx+1][cy+1]!=1:
                    l[cx][cy]=1
                    l[cx+1][cy]=1
                    l[cx+1][cy+1]=1
                    l[cx-1][cy]=1
                    l[cx-1][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==32:
                if l[cx][cy]!=1 and cx+1 in l and cy-1>=0 and cy+1<len(l[cx]) and l[cx][cy-1]!=1 and l[cx][cy+1]!=1 and l[cx+1][cy+1]!=1:
                    l[cx][cy]=1
                    l[cx][cy-1]=1
                    l[cx][cy+1]=1
                    l[cx+1][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==33:
                if l[cx][cy]!=1 and cx+1 in l and cy-1>=0 and cy+1<len(l[cx]) and l[cx][cy-1]!=1 and l[cx][cy+1]!=1 and l[cx+1][cy-1]!=1:
                    l[cx][cy]=1
                    l[cx][cy-1]=1
                    l[cx][cy+1]=1
                    l[cx+1][cy-1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==34:
                if l[cx][cy]!=1 and cx-1 in l and cy-1>=0 and cy+1<len(l[cx]) and l[cx][cy-1]!=1 and l[cx][cy+1]!=1 and l[cx-1][cy-1]!=1:
                    l[cx][cy]=1
                    l[cx][cy-1]=1
                    l[cx][cy+1]=1
                    l[cx-1][cy-1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==35:
                if l[cx][cy]!=1 and cx-1 in l and cy-1>=0 and cy+1<len(l[cx]) and l[cx][cy-1]!=1 and l[cx][cy+1]!=1 and l[cx-1][cy+1]!=1:
                    l[cx][cy]=1
                    l[cx][cy-1]=1
                    l[cx][cy+1]=1
                    l[cx-1][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==36:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy-1>=0 and l[cx+1][cy]!=1 and l[cx-1][cy]!=1 and l[cx+1][cy-1]!=1:
                    l[cx][cy]=1
                    l[cx+1][cy]=1
                    l[cx+1][cy-1]=1
                    l[cx-1][cy]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==37:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy-1>=0 and l[cx+1][cy]!=1 and l[cx-1][cy]!=1 and l[cx-1][cy-1]!=1:
                    l[cx][cy]=1
                    l[cx+1][cy]=1
                    l[cx-1][cy-1]=1
                    l[cx-1][cy]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==38:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy+1<len(l[cx]) and l[cx+1][cy]!=1 and l[cx-1][cy]!=1 and l[cx+1][cy+1]!=1:
                    l[cx][cy]=1
                    l[cx+1][cy]=1
                    l[cx+1][cy+1]=1
                    l[cx-1][cy]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==39:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy+1<len(l[cx]) and l[cx+1][cy]!=1 and l[cx-1][cy]!=1 and l[cx-1][cy+1]!=1:
                    l[cx][cy]=1
                    l[cx+1][cy]=1
                    l[cx-1][cy+1]=1
                    l[cx-1][cy]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==40:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy-1>=0 and cy+1<len(l[cx]) and l[cx][cy-1]!=1 and l[cx][cy+1]!=1 and l[cx-1][cy+1]!=1 and l[cx+1][cy-1]!=1:
                    l[cx][cy]=1
                    l[cx][cy-1]=1
                    l[cx][cy+1]=1
                    l[cx+1][cy-1]=1
                    l[cx-1][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==41:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy+1<len(l[cx]) and cy-1>=0 and l[cx][cy+1]!=1 and l[cx][cy-1]!=1 and l[cx+1][cy+1]!=1 and l[cx-1][cy-1]!=1:
                    l[cx][cy]=1
                    l[cx-1][cy-1]=1
                    l[cx][cy-1]=1
                    l[cx][cy+1]=1
                    l[cx+1][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==42:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy-1>=0 and cy+1<len(l[cx]) and l[cx-1][cy]!=1 and l[cx-1][cy+1]!=1 and l[cx+1][cy]!=1 and l[cx+1][cy-1]!=1:
                    l[cx][cy]=1
                    l[cx-1][cy]=1
                    l[cx-1][cy+1]=1
                    l[cx+1][cy]=1
                    l[cx+1][cy-1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==43:
                if l[cx][cy]!=1 and cx+1 in l and cx-1 in l and cy-1>=0 and cy+1<len(l[cx]) and l[cx-1][cy]!=1 and l[cx-1][cy-1]!=1 and l[cx+1][cy]!=1 and l[cx+1][cy+1]!=1:
                    l[cx][cy]=1
                    l[cx-1][cy]=1
                    l[cx-1][cy-1]=1
                    l[cx+1][cy]=1
                    l[cx+1][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==44:
                if l[cx][cy]!=1 and cx-1 in l and cy+1<len(l[cx]) and l[cx][cy+1]!=1 and l[cx+1][cy+1]!=1:
                    l[cx][cy]=1
                    l[cx+1][cy+1]=1
                    l[cx][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==45:
                if l[cx][cy]!=1 and cx-1 in l and cy+1<len(l[cx]) and l[cx][cy+1]!=1 and l[cx-1][cy+1]!=1:
                    l[cx][cy]=1
                    l[cx][cy+1]=1
                    l[cx-1][cy+1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==46:
                if l[cx][cy]!=1 and cx+1 in l and cy-1>=0 and l[cx][cy-1]!=1 and l[cx+1][cy-1]!=1:
                    l[cx][cy]=1
                    l[cx+1][cy-1]=1
                    l[cx][cy-1]=1
                    return 0
                else:
                    return 1
                f1=-1
            elif i==47:
                if l[cx][cy]!=1 and cx-1 in l and cy-1>=0 and l[cx][cy-1]!=1 and l[cx-1][cy-1]!=1:
                    l[cx][cy]=1
                    l[cx-1][cy-1]=1
                    l[cx][cy-1]=1
                    return 0
                else:
                    return 1
                f1=-1
font_name=pygame.font.match_font('comicsansms')
def draw_text(surf,text,size,x,y,c):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,(c))
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surf.blit(text_surface,text_rect)
r=True
t=0
l={}
v=0
sc=0
sk=1
ms=0
se=0
go=0
x0=random.randint(1,11)
x1=random.randint(12,21)
x2=random.randint(22,31)
x3=random.randint(32,47)
x4=1
xl=[x0,x1,x2,x3,x4]
xi=random.choice(xl)
cou=0
for i in range(11):
    l[i]=[0,0,0,0,0,0,0,0,0,0,0]
while r:
    scr.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = False
    if go==0:
        pygame.draw.rect(scr,(255,155,0),(240,275,70,50))
        pygame.draw.polygon(scr,(255,255,255),[(260,285),(290,300),(260,315)])
        m=pygame.mouse.get_pressed()
        p=pygame.mouse.get_pos()
        if m[0]==1 and p[1]>277 and p[1]<324 and p[0]>242 and p[0]<309:
            t=0
            v=0
            sc=0
            sk=1
            ms=0
            se=0
            go=1
            m=()
            p=()
            x=275
            y=550
            w=15
            h=15
            cx=0
            cy=0
            f1=-1
            for i in range(11):
                l[i]=[0,0,0,0,0,0,0,0,0,0,0]
            x0=random.randint(1,11)
            x1=random.randint(12,21)
            x2=random.randint(22,31)
            x3=random.randint(32,47)
            x4=1
            xl=[x0,x1,x2,x3,x4]
            xi=random.choice(xl)
            cou=0
    if go==1:
        m=pygame.mouse.get_pressed()
        p=pygame.mouse.get_pos()
        grid()
        for i in range(11):
            co=0
            if l[i].count(1)==11:
                for j in range(11):
                    l[i][j]=0
            for j in range(11):
                if l[j][i]==1:
                    co+=1
            if co==11:
                for j in range(11):
                    l[j][i]=0
        for i in l:
            for j in range(len(l[i])):
                if l[i][j]==1:
                    pygame.draw.rect(scr,(255,0,0),((j*35+80),(i*35+75),30,30))
                else:
                    pygame.draw.rect(scr,(190,190,190),((j*35+80),(i*35+75),30,30))
        if v==0:
            x0=random.randint(1,11)
            x1=random.randint(12,21)
            x2=random.randint(22,31)
            x3=random.randint(32,47)
            x4=1
            xl=[x0,x1,x2,x3,x4]
            xi=random.choice(xl)
            v=1
        if cou>=25:
            v=stat(xi,l)
        if v==0:
            sc+=score(i)
        if sk==1:
            pygame.draw.rect(scr,(0,255,255),(30,20,50,30))
            draw_text(scr,'Skip',20,55,20,(0,0,0))
            if m[0]==1 and p[0]>32 and p[0]<78 and p[1]>22 and p[1]<48:
                v=0
                sk=0
        pygame.draw.rect(scr,(255,155,0),(25,70,5,385))
        pygame.draw.rect(scr,(255,155,0),(60,70,5,385))
        pygame.draw.rect(scr,(255,155,0),(25,70,40,5))
        pygame.draw.rect(scr,(255,155,0),(25,455,40,5))
        ms+=1
        if ms==200:
            se+=1
            ms=0
        for i in range(se):
            pygame.draw.rect(scr,(0,255,0),(30,75,30,-5+se*35))
        if v==0:
            se=0
        if se>=11:
            go=0
        cou=cou+1
    draw_text(scr,str(sc),50,275,0,(255,255,255))
    pygame.display.update()
pygame.quit()
    
                        
                    
