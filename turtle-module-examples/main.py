from turtle import Turtle, Screen
from diagram import Shape

tim_the_turtle = Turtle()
tim_the_turtle.shape('arrow')

screen = Screen()
screen.colormode(255)

# Create only square
s = Shape()
s.square(tim_the_turtle)
screen.resetscreen()

# Create All shapes
for side in range(3, 11):
    angle = 360 / side
    s.create_shape(tim_the_turtle, side, angle)

# Create dashed line
screen.resetscreen()
s.dashed_line(tim_the_turtle, 10)

# Create random line directions
screen.resetscreen()
s.random_shape(tim_the_turtle)

# Create spirograph
screen.resetscreen()
s.draw_spirograph(tim_the_turtle, 5)

## Create Hirst Diagram
screen.resetscreen()
s.hirst_diagram(tim_the_turtle)

screen.exitonclick()
