import turtle
from random import randint 
import time
import array as array

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

def shoot():
    xpozicio=urhajo.xcor()
    ypozicio=urhajo.ycor()
    laser.setx(xpozicio)
    laser.sety(ypozicio)

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
space.addshape("laser.gif")
space.tracer(0)
space.listen()
space.onkey(fel ,"Up")
space.onkey(le ,"Down")
space.onkey(balra ,"Left")
space.onkey(jobbra ,"Right")
space.onkey(shoot, "space")

urhajo= turtle.Turtle()
urhajo.shape("sprite.gif")
urhajo.penup()

meteor1=turtle.Turtle()
meteor1.shape("meteor1.gif")
meteor1.penup()
meteor1.setx(400)
meteor1.sety(randint(-30,30)*10)
#meteor1.sety(0)

laser=turtle.Turtle()
laser.shape("laser.gif")
laser.penup()

tureshatarok = array.array('i', [ -40,-30, -20, -10, 0, 10, 20, 30, 40,])
readytoshoot=True
szamlalo=0
eletszamlalo=10
while eletszamlalo!=0:
    

    while meteor1.xcor() > -400:
        space.update()
        meteor_mozgas = meteor1.xcor()
        meteor_mozgas -= 5
        time.sleep(0.01)
        
        meteor1.setx(meteor_mozgas)

        eletkijelzo.write(f"Életeid: {eletszamlalo}", align="center", font=("Arial", 30, "bold"))
        
        for t in tureshatarok:
            if meteor1.xcor()==urhajo.xcor()+t:
                for t in tureshatarok:
                    if meteor1.ycor()==urhajo.ycor()+t:
                        eletkijelzo.clear()
                        eletszamlalo-=1
                        meteor1.setx(400)
                        meteor1.sety(randint(-30,30)*10)
            

        if eletszamlalo==0:
            kijelzo.goto(0,0)
            kijelzo.write("GAME OVER", align="center", font=("Arial", 60, "bold"))
            urhajo.setx(10000)
            urhajo.sety(10000)


        if readytoshoot==True:
            laser_mozgas=laser.xcor()
            readytoshoot=False
            laser_mozgas_ycor=laser.ycor()

        if laser_mozgas>400:
            readytoshoot=True
        
        laser_mozgas+=10
        laser.setx(laser_mozgas)
        laser.sety(laser_mozgas_ycor)
        
        for t in tureshatarok:
            if meteor1.xcor()==laser.xcor()+t:
                for t in tureshatarok:
                    if meteor1.ycor()==laser.ycor()+t:
                        kijelzo.clear()
                        szamlalo+=1
                        meteor1.setx(400)
                        meteor1.sety(randint(-30,30)*10)
                        #meteor1.sety(0)
                        laser_mozgas=450

        kijelzo.clear()
        kijelzo.write(f"Pontjaid: {szamlalo}", align="center", font=("Arial", 30, "bold"))       

    
    while meteor1.xcor() <= -400:
        
        if meteor1.xcor()==-400:
            meteor1.setx(400)
            meteor1.sety(randint(-30,30)*10)
            #meteor1.sety(0)
            

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
        time.sleep(0.01)
        

        if eletszamlalo==0:
            time.sleep(5)
