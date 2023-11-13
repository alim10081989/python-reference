import random
from extract import color_extract

class Shape:

    def __init__(self, steps=50, angle=90):
        self.steps = steps
        self.angle = angle

    def random_color(self):
        """
        Select random color and return
        :return:
        """
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        return color

    def square(self, tim_turtle):
        """
        Create a square shape
        :param tim_turtle:
        :return:
        """
        tim_turtle.pensize(10)
        tim_turtle.speed("fastest")
        tim_turtle.color(self.random_color())
        for _ in range(4):
            tim_turtle.forward(self.steps)
            tim_turtle.right(self.angle)

    def dashed_line(self, tim_turtle, steps):
        """
        Create dashed line
        :param tim_turtle:
        :param steps:
        :return:
        """
        tim_turtle.speed("fastest")
        tim_turtle.pensize(10)
        tim_turtle.color(self.random_color())
        for _ in range(20):
            tim_turtle.forward(steps)
            tim_turtle.penup()
            tim_turtle.forward(steps)
            tim_turtle.pendown()

    def create_shape(self, tim_turtle, no_of_sides, angle):
        """
        Create all shapes with multiple sides
        :param tim_turtle:
        :param no_of_sides:
        :param angle:
        :return:
        """
        tim_turtle.speed("fastest")
        tim_turtle.color(self.random_color())
        for _ in range(no_of_sides):
            tim_turtle.forward(50)
            tim_turtle.right(angle)

    def random_shape(self, tim_turtle):
        """
        Draw shapes in random directions
        :param tim_turtle:
        :return:
        """
        direction = [0, 90, 180, 270]
        tim_turtle.pensize(10)
        tim_turtle.speed("fastest")
        for _ in range(200):
            tim_turtle.color(self.random_color())
            tim_turtle.forward(30)
            tim_turtle.setheading(random.choice(direction))

    def draw_spirograph(self, tim_turtle, size_of_gap):
        """
        Draw Spirograph
        :param tim_turtle:
        :param size_of_gap:
        :return:
        """
        tim_turtle.speed("fastest")
        for _ in range(int(360 / size_of_gap)):
            tim_turtle.color(self.random_color())
            tim_turtle.circle(100)
            tim_turtle.setheading(tim_turtle.heading() + size_of_gap)


    def hirst_diagram(self, tim_turtle):
        """
        Draw a hirst diagram
        :param tim_turtle:
        :return:
        """
        tim_turtle.penup()
        tim_turtle.hideturtle()
        tim_turtle.speed('fastest')
        tim_turtle.setheading(225)
        tim_turtle.forward(300)
        tim_turtle.setheading(0)
        number_of_dots = 100

        ce = color_extract()
        color_palette = ce.extract_colors()

        for dot_count in range(1, number_of_dots + 1):
            tim_turtle.dot(20, random.choice(color_palette))
            tim_turtle.forward(50)

            if dot_count % 10 == 0:
                tim_turtle.setheading(90)   # Turn left to 90 degree
                tim_turtle.forward(50)      # Move forward 50 paces
                tim_turtle.setheading(180)  # Turn left to 180 degree
                tim_turtle.forward(500)     # Move forward 10 dots X 50 paces
                tim_turtle.setheading(0)    # Turn right to 0 degree
