import turtle
from random import randint 
import time

def fel():
    ypozicio=urhajo.ycor()
    ypozicio+=10
    urhajo.sety(ypozicio)

def le():
    ypozicio=urhajo.ycor()
    ypozicio-=10
    urhajo.sety(ypozicio)

def jobbra():
    xpozicio=urhajo.xcor()
    xpozicio+=10
    urhajo.setx(xpozicio)

def balra():
    xpozicio=urhajo.xcor()
    xpozicio-=10
    urhajo.setx(xpozicio)

kijelzo = turtle.Turtle()
kijelzo.hideturtle()
kijelzo.penup()
kijelzo.goto(0,260) 
kijelzo.color("white")

eletkijelzo=turtle.Turtle()
eletkijelzo.hideturtle()
eletkijelzo.penup()
eletkijelzo.goto(0,-260) 
eletkijelzo.color("white")


space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("background.png")
space.addshape("sprite.gif")
space.addshape("meteor1.gif")
space.tracer(0)
space.listen()
space.onkey(fel ,"Up")
space.onkey(le ,"Down")
space.onkey(balra ,"Left")
space.onkey(jobbra ,"Right")

urhajo= turtle.Turtle()
urhajo.shape("sprite.gif")
urhajo.penup()

meteor1=turtle.Turtle()
meteor1.shape("meteor1.gif")
meteor1.penup()
meteor1.setx(400)
meteor1.sety(randint(-30,30)*10)

szamlalo=0
eletszamlalo=1
while eletszamlalo!=0:
    

    while meteor1.xcor() > -400:
        space.update()
        time.sleep(0.05)
        meteor_mozgas = meteor1.xcor()
        meteor_mozgas -= 10
        meteor1.setx(meteor_mozgas)

        eletkijelzo.write(f"Életeid: {eletszamlalo}", align="center", font=("Arial", 30, "bold"))
        
        if meteor1.xcor()==urhajo.xcor() and meteor1.ycor()==urhajo.ycor():
            eletkijelzo.clear()
            eletszamlalo-=1
            meteor1.setx(400)
            meteor1.sety(randint(-30,30)*10)
            

        if eletszamlalo==0:
            kijelzo.goto(0,0)
            kijelzo.write("GAME OVER", align="center", font=("Arial", 60, "bold"))
            urhajo.setx(10000)
            urhajo.sety(10000)
    
    while meteor1.xcor() <= -400:
        
        if meteor1.xcor()==-400:
            meteor1.setx(400)
            meteor1.sety(randint(-30,30)*10)
            if eletszamlalo!=0:
                szamlalo+=1

        kijelzo.clear()
        kijelzo.write(f"Pontjaid: {szamlalo}", align="center", font=("Arial", 30, "bold"))
        
        if urhajo.ycor()>300:
            urhajo.sety(-300)
        
        if urhajo.ycor()<-300:
            urhajo.sety(300)
        
        if urhajo.xcor()>400:
            urhajo.setx(-400)
        
        if urhajo.xcor()<-400:
            urhajo.setx(400)

        space.update()
        time.sleep(0.2)
        

        if eletszamlalo==0:
            time.sleep(5)
