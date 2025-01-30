
from turtle import *
import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Game")
wn.setup(700,700)
#create pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold=0

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()


        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def collide(self, other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2) )

            if distance < 5:
                return True
            else:
                return False

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



levels = [""]

level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXX",
"XP   XXXXXXX          XXXX",
"X   XXXXXXX  XXXXX   XXXXX",
"X        XX  XXXXX   XXXXX",
"X        XX  XXX        XX",
"XXXXXX   XX  XXX        XX",
"XXXXXX   XX  XXXXX  XXXXXX",
"XXXXXX   XX    XXX  XXXXXX",
"X  XXX         XXX  XXXXXX",
"X  XXX   XXXXXXXXXXXXXXXXX",
"X          XXXXXXXXXXXXXXX",
"X                 XXXXXXXX",
"XXXXXXXXXXXXX     XXXXXT  X",
"XXXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXXX         X",
"XXX                      X",
"XXX            XXXXXXXXXXX",
"XXXXXXXXXXX    XXXXXXXXXXX",
"XXXXXXXXXXX              X",
"XX                       X",
"X     XXXXXXXXXXXXXXXXXXXX",
"X          XXXXXXXXXXXXXXX",
"XXXXXX     XXXXXXXXXXXXXXX",
"X          XXXXXXXXXXXXXXX",
"X    XXXXXXXXXXXXXXXXXXXXX",
"X          XXXXXXXXXXXXXXX",
]

treasures = []

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
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

pen = Pen()
player = Player()

walls = []

setup_maze(levels[1])

turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

wn.tracer(0)


while True:

    for treasure in treasures:
        if player.collide(treasure):

            player.gold += treasure.gold
            print ("Player Gold: {}".format(player.gold))

            treasure.destroy()

            treasures.remove(treasure)

    wn.update()





