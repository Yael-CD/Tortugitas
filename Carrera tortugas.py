from turtle import *
import turtle
t3=Turtle()
t3.shape("turtle")
tMeta=Turtle()

#Dibujar la Meta
tMeta.speed(200)
num_lineas = 2 
contador = 0
incre=25

tMeta.penup()
tMeta.goto(350,300)
tMeta.pendown()
tMeta.left(270)

while contador < num_lineas:
    if contador==1:
        tMeta.penup()
        tMeta.goto(350+incre,300)  # Mover a la posición de inicio para cada línea
        tMeta.pendown()
        tMeta.left(0)
        
    for i in range(25):
        if (i % 2 == 0):
            tMeta.color("black", "red")
        else:
            tMeta.color("black", "white") 
        tMeta.begin_fill()
        for _ in range(4):
            tMeta.forward(25)
            tMeta.right(90)
        tMeta.end_fill()
        tMeta.penup()
        tMeta.forward(25)
        tMeta.pendown()
    contador += 1

#Dibujar la T2
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.speed(8)  

# Posición inicial
t.penup()
t.goto(-300, 0)  # Inicia en (-400, 0)
t.pendown()

radio = 10 

for _ in range(30):  
    t.circle(radio) 
    t.penup()
    t.goto(t.xcor() + radio * 2, 0) 
    t.pendown()
    radio += 2 


#Dibujar la T3
t3.penup()
t3.goto(-400,-280)
t3.pendown()
t3.color("blue","white")
incre=0
t3.speed(30)
for i in range (7):
    incre=incre+100
    for i in range (4):
        t3.forward(100)
        t3.right(90)
    t3.goto(-400+incre,-280)
    for i in range (3):
        t3.forward(100)
        t3.left(-120)
    t3.circle(30)
    
for i in range (4):
    t3.forward(100)
    t3.right(90)
done()
