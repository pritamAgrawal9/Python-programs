from turtle import Turtle
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.boxes = []
        self.create_snake()
        self.head = self.boxes[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_box(position)

    def add_box(self, position):
        box = Turtle("square")
        box.color("white")
        box.penup()
        box.goto(position)
        self.boxes.append(box)
    def extend(self):
        self.add_box(self.boxes[-1].position())

    def move(self):
        for go in range(len(self.boxes) - 1, 0, -1):
            new_x = self.boxes[go - 1].xcor()
            new_y = self.boxes[go - 1].ycor()
            self.boxes[go].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


