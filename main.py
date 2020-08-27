import turtle
import random

t_rotation = ''
t_length = ''

class branch:

    def __init__(self, rotation, length):
        t = turtle.Turtle()
        t.hideturtle()
        t.pensize(2)
        t.speed(9)

        rotation = random.randint(1, 180)
        t.lt(rotation)
        length = random.randint(100, 150)
        t.fd(length)

        for i in range(2):
            rotation = random.randint(7, 14)
            t.lt(rotation)
            t.fd(length)

def base_setup():
    base = turtle.Turtle()
    base.penup()
    base.pensize(2 )
    base.hideturtle()
    base.speed(0)
    base.setheading(90)
    base.goto(0, -500)
    base.pendown()
    base.fd(500)

base_setup()

a = branch(t_rotation, t_length)
b = branch(t_rotation, t_length)
c = branch(t_rotation, t_length)
d = branch(t_rotation, t_length)
e = branch(t_rotation, t_length)
f = branch(t_rotation, t_length)
g = branch(t_rotation, t_length)
h = branch(t_rotation, t_length)
i = branch(t_rotation, t_length)
j = branch(t_rotation, t_length)
k = branch(t_rotation, t_length)