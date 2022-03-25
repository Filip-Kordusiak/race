import turtle
from turtle import Turtle,Screen
import random
isRaceOn = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="lol", prompt="xddd:")
tim = Turtle(shape="turtle")
tim.color("red")
tim.penup()
tim.goto(-240, 180)
tim.forward(10)

tom = Turtle(shape="turtle")
tom.color("green")
tom.penup()
tom.goto(-240, 0)
tom.forward(10)

tam = Turtle(shape="turtle")
tam.color("blue")
tam.penup()
tam.goto(-240, -180)
tam.forward(10)

if bet:
    isRaceOn = True
all_turtle = [tom, tam, tim]
while isRaceOn:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            isRaceOn = False

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



print(bet)
print(winner)
screen.exitonclick()
