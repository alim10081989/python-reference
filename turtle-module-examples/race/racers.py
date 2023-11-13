from turtle import Turtle
import random

COLORS = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
POSITION_Y = [-70, -40, -10, 20, 50, 80]


class Racers(Turtle):
    def __init__(self):
        super().__init__()
        self.all_turtles = []
        self.hideturtle()

    def create_racers(self):
        for i in range(len(COLORS)):
            new_turtle = Turtle(shape='turtle')
            new_turtle.color(COLORS[i])
            new_turtle.penup()
            new_turtle.goto(x=-380, y=POSITION_Y[i])
            self.all_turtles.append(new_turtle)
            i -= 1

    def turtle_race(self):
        random_distance = random.randint(0, 10)
        turtle = random.choice(self.all_turtles)
        turtle.forward(random_distance)

        if turtle.xcor() > 380:
            return turtle.pencolor()

