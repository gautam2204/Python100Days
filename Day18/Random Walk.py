from turtle import Turtle, Screen
import random

tur = Turtle()
directions = [0, 90, 180, 270]
sc = Screen()
sc.screensize(200,300)
def rightTurn():
    tur.right(random.choice(directions))

def leftTurn():
    tur.left(random.choice(directions))

def backward():
    tur.backward(random.choice(directions))

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


methods = [{
    "right": leftTurn},
    {"left": rightTurn}
]
count = 200
tur.pensize(8)
tur.speed(8)
tur.setheading(90)

while count > 0:
    tur.color(random.choice(colours))
    tur.forward(30)
    randVal=random.choice(methods)
    for key in randVal:
        randVal[key]()
    count -= 1
