# CTI 110
# P4LAB1 - Turtle
# CastroPerez_Jesus
# 10/6/26

import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("P4LAB1")
screen.bgcolor("black")

t = turtle.Turtle()
t.color("blue")
t.shape("turtle")
t.pencolor("blue")
t.fillcolor("orange")
t.pensize(3)

sides = 4
angle = 360 / sides
length = 100
with t.fill():
    while sides > 0:
        t.forward(100)
        t.right(90)
        sides = sides - 1

sides = 3
t.fillcolor("red")
t.begin_fill()
for side in range(sides):
    t.forward(100)
    t.left(120)
t.end_fill()

t.teleport(-200, 0)
sides = 4
t.fillcolor("orange")
t.begin_fill()
for side in range(sides):
    t.forward(length)
    t.right(angle)
t.end_fill()

sides = 3
t.fillcolor("red")
t.begin_fill()
for side in range(sides):
    t.forward(100)
    t.left(120)
t.end_fill()

t.penup()
t.goto(200, 180)
t.pendown()

t.fillcolor("gold")
t.pencolor("gold")
t.begin_fill()
for point in range(5):
    t.forward(80)
    t.right(144)
t.end_fill()

turtle.done()