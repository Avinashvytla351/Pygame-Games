import turtle
import time
t=turtle.Turtle()
l=turtle.Turtle()
t1=turtle.Screen()
l1=turtle.Screen()
t.pensize(30)
t.speed(10.5)
t.setheading(180)
t1.bgcolor("black")
t.ht()
l.ht()
l.speed(10.5)
l1.tracer(0)
def tim(s,m,h,v):
    t.penup()
    t.setheading(180)
    t.goto(0,230) 
    t.pendown()
    t.color("red")
    t.circle(250,s)
    print(s)
    if(s==-0.0):
        t.clear()
    t.penup()
    t.goto(0,230)
    t.setheading(180)
    t.pendown()
    l.penup()
    l.goto(0,-20)
    l.setheading(90)
    l.color("orange")
    l.pendown()
    l.rt(-s)
    l.pensize(5)
    l.backward(25)
    l.fd(320)
    l.pensize(8)
    l.fd(5)
    t.penup()
    t.goto(0,190)
    t.setheading(180)
    t.pendown()
    t.color("lightgreen")
    t.circle(210,m)
    if(m==-0.0):
        t.clear()
    t.penup()
    t.goto(0,190)
    t.setheading(180)
    t.pendown()
    l.penup()
    l.goto(0,-20)
    l.setheading(90)
    l.color("white")
    l.pendown()
    l.rt(-m)
    l.pensize(5)
    l.fd(30)
    l.pensize(15)
    l.forward(235)
    t.penup()
    t.goto(0,150)
    t.setheading(180)
    t.pendown()
    t.color("skyblue")
    t.circle(170,h)
    if(h==-30 and v<1 and m==-6):
        t.clear()
        v=v+1
    t.penup()
    t.goto(0,150)
    t.setheading(180)
    t.pendown()
    l.penup()
    l.goto(0,-20)
    l.setheading(90)
    l.color("white")
    l.pendown()
    l.rt(-h)
    l.pensize(5)
    l.fd(30)
    l.pensize(15)
    l.forward(170)
while(True):
    c=turtle.Turtle()
    c.ht()
    c.color("grey")
    c.penup()
    c.pensize(20)
    c.goto(0,265)
    c.pendown()
    c.circle(-285)
    c.penup()
    c.goto(0,-20)
    c.setheading(180)
    for i in range(12):
        c.fd(270)
        c.pendown()
        c.pensize(3)
        c.color("white")
        c.fd(30)
        c.penup()
        c.goto(0,-20)
        c.left(30)
    c.penup()
    c.goto(0,-13)
    c.pensize(5)
    c.color("white")
    c.pendown()
    c.circle(7)
    c.penup()
    c.goto(0,-15)
    c.color("orange")
    c.pendown()
    c.circle(5)
    s = int(time.strftime("%S"))
    m=int(time.strftime("%M"))
    h=int(time.strftime("%I"))
    a=(s/60)*360
    b=(m/60)*360
    c=(h/12)*360
    v=0
    print(s,a)
    tim(-a,-b,-c,v)
    l1.update()
    time.sleep(1)
    l.clear()
