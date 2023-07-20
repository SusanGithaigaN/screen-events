from turtle import Turtle, Screen

spice = Turtle()
screen = Screen()

# start listening
screen.listen()
# bind a function to a keystroke
def move_foward():
    spice.forward(10)

screen.onkey(key= "space", fun=move_foward)
screen.exitonclick()
