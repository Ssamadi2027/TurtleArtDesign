import turtle#brings in the turtle which draws your results
from project_2nd import *

turtle.colormode(255)#allows you to use colors from the RGB color scheme.
turtle.bgcolor(0,0,0)

bob=turtle.Turtle()
bob.speed(0)

bob.color(255,255,255)

bob.penup()
bob.goto(0,0)
bob.pendown()

for times in range(180):
    bob.forward(1000)
    bob.goto(0,0)
    bob.right(2)

bob.color(0,0,255)

spiral(bob,50,38,90)

for times in range(90):
    bob.color(255,0,0)
    bob.circle(200)
    bob.right(4)
bob.penup()
bob.goto(0,150)
bob.pendown()
bob.color(0,255,0)

spiral(bob,50,38,90)

bob.penup()
bob.goto(150,0)
bob.pendown()

bob.color(255,255,0)

spiral(bob,50,38,90)

bob.penup()
bob.goto(-150,0)
bob.pendown()

bob.color(255,255,0)

spiral(bob,50,38,90)

bob.penup()
bob.goto(0,-150)
bob.pendown()

bob.color(0,255,0)

spiral(bob,50,38,90)

bob.color(0,255,255)

bob.penup()
bob.goto(400,400)
bob.pendown()

for times in range(20):
    triangle(bob,100,144)
    bob.right(1)

bob.penup()
bob.goto(-400,400)
bob.pendown()

for times in range(20):
    triangle(bob,100,144)
    bob.right(1)


bob.penup()
bob.goto(400,-400)
bob.pendown()

for times in range(20):
    triangle(bob,100,144)
    bob.right(1)

bob.penup()
bob.goto(-400,-400)
bob.pendown()


for times in range(20):
    triangle(bob,100,144)
    bob.right(1)

bob.penup()
bob.goto(400,0)
bob.pendown()

for times in range(20):
    triangle(bob,100,144)
    bob.right(1)

bob.penup()
bob.goto(-470,0)
bob.pendown()


for times in range(20):
    triangle(bob,100,144)
    bob.right(1)















    







    












