from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [135, 81, 27, -27, -81, -135]
new_turtle_list = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-240,y=y_positions[i])
    new_turtle_list.append(new_turtle)
        
    
if user_bet:
    is_race_on =True

while is_race_on:
    
    for turtle in new_turtle_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")
            is_race_on = False
    
        rand_distance = randint(0,10)
        turtle.forward(rand_distance)
    


screen.exitonclick()