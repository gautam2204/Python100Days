from turtle import Turtle,Screen

tim = Turtle()
tim.shape("turtle")
tim.color("Red")
screen = Screen()

for i in range(1,5):
    for j in range(1,100,1):
        tim.forward(j)
        tim.penup()
        tim.right(j)
        tim.pendown()






screen.exitonclick()











