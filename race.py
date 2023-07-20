import turtle
from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
# setup width and height
screen.setup(width=700, height=800)
# bring popp to ask user to make a bet
bet = screen.textinput(title="Make your bet", prompt="Which tutle will wil the race? Enter a color: ")
# print(bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "magenta", "pink", "violet", "aqua"]

y_positions = [-70, -40, -10, 20, 50, 80, 110, 140, 170, 200]
all_turtles = []

for turtle_index in range(0, 10):
    # move turtle to start of line
    new_turtle = Turtle(shape="turtle")
    # not draw
    new_turtle.penup()
    # set turtle index
    new_turtle.goto(x=-330, y=y_positions[turtle_index])
    # create a list of colors
    new_turtle.color(colors[turtle_index])
    # append a new turtle to the list everytime it is created
    all_turtles.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:
    # loop through turtle list
    for turtle in all_turtles:
        if turtle.xcor() >330:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won. The {winning_color} turtle is the winner!!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!!")
        # get hold of a random num
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        # stop turtles when they reach the end of the screen/finish race

screen.exitonclick()