from turtle import Turtle, Screen


timmy = Turtle()
screen = Screen()
print(screen.canvwidth)
print(timmy)
timmy.color("red")
print(timmy.xcor(),timmy.ycor())
timmy.forward(100)


screen.exitonclick()


