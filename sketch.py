 # w = Fowards
 # s= backwards
 # a = counter-clockwise
 # d =clockwise
 # c - clear drawing

from turtle import Turtle, Screen

sketch = Turtle()
screen = Screen()
# start listening
screen.listen()
# bind a function to a keystroke
# prompt user to enter a keystroke

def move_foward():
    sketch.forward(10)
def move_backward():
    sketch.backward(10)

def turn_left():
    # new_heading = sketch.heading() + 10
    # sketch.setheading((new_heading))
    sketch.left(10)

def turn_right():
    sketch.right(10)

def clear():
    sketch.clear()
    # bring turtle back to starting point
    sketch.penup()
    sketch.home()
    sketch.pendown()

# movements
screen.listen()
screen.onkey(move_foward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()