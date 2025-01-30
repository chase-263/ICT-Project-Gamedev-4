from random import random
from turtle import *
from freegames import line
import turtle


#
# def draw():
#     color('red')
#     width (8)
#
#     for x in range (-205, 205, 40):
#         for z in range (-205, 205, 40):
#             if random () > 0.5:
#                 line (x, z , x+40, z+45)
#             else:
#                 line(x, z+45, x+45, z)
# update()
#
# def tap(x,z):
#
#     if abs(x) > 198 or abs (z) > 198:
#         up()
#     else:
#         down()
#     width(2)
#     color("brown")
#     goto(x, z)
#     dot(4)
#
# setup (420, 420, 370, 0)
# hideturtle()
# tracer(False)
# draw()
# onscreenclick(tap)
# done()

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("A MAZE GAME BY TOBI")
wn.setup(700,700)
class Pen(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("white")
            self.penup()
            self.speed(0)
levels=[""]

level_1=[
    "XXXXXXXXX    XXXXXXXXXXXXXXXX",
    "XXXXXXX         XXXXXXXXXXXX",
    "XXXXXXX         XXXXXXXXXXX",
    "XXXXXXX            XXXXXXXXXXX",
    "XXXXXXX    XXXXX    XXXXXXXXXX",
    "XXXXXXXX    XXXX        XXXXXX",
    "XXXXXXX     XXXX         XXXXXX",
    "XXX      XXXXXXXXX       XXXXXX",
    "XXX     XXXXXXX          XXXXXX",
    "XXX     XXXXXXX          XXXXXXX",
    "XXX     XXXXXXX     XXXXXXXXXXXX",
    "XXXX              XXXXXXXXXXXX",
    "XXXXXXXXXX     XXXXXXXXXXXX",
    "XXXXXXXXXX     XXXXXXXXXXXX",
    "XXXXXXXXXX     XXXXXXXXXXXX"
    "XXXXXX         XXXXXXXXXXXX",
    "XXXXXX         XXXXXXXXXXXX",
    "XXXXX      XXXXXXXXXXXXXXXX",
    "XXXXX      XXXXXXXXXXXXXXXX",
    "XXXXX      XXXXXXXXXXXXXXXX"
    "XXXXX      XXXXXXXXXXXXXXXX",
    "XXXXX              XXXXXXXX",
    "XXXXX             XXXXXXXX",
    "XXXXXXXXXXX        XXXXXXXX",
    "XXXXXXXXXXX        XXXXXXXX"
]
levels.append(level_1)
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character=level[y][x]
            screen_x=-288+(x*24)
            screen_y=-288+(y*24)
            if character=="X":
                pen.goto(screen_x,screen_y)
                pen.stamp()

pen=Pen()
setup_maze(levels[1])
while True:
    pass