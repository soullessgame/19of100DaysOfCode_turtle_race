from turtle import Turtle, Screen
import random

is_race_on=False
screen=Screen()
screen.colormode(255)
screen.setup(width=500, height=400)
user_bet=screen.textinput("bet", "Which turtle is going to win? Enter a colour: ")
print(user_bet)
colors=["red", "orange", "yellow", "green", "blue","purple"]
y_positions=[-70, -40, -10, 20, 50, 80]
turtles=[]

for turtle_index in range(0, 6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    turtles.append(new_turtle)

# print(turtles[1].color())
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() >= 230:
            winner_color=turtle.pencolor()
            is_race_on= False
            break
print(f'the {winner_color} turtle has won the race')

if winner_color == user_bet:
    print(f'your turtle, the {user_bet} coloured turtle won')
else:
    print(f'your turtle, the {user_bet} coloured turtle lost')

screen.exitonclick()