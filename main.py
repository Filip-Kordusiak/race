from turtle import Screen, Turtle

tom = Turtle()
screen = Screen()

def move_forwards():
    tom.forward(10)
def move_backward():
    tom.backward(10)
def clockwise():
    nowe = tom.heading() - 30
    tom.setheading(nowe)
def counter_clockwise():
    tom.left(30)
def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=clockwise)
screen.onkey(key="d", fun=counter_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

