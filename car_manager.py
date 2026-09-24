from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
HEADING = 180


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(HEADING)
        self.starting_position()
        self.move_speed = 0.1

    def drive(self):
        self.forward(MOVE_INCREMENT)

    def starting_position(self):
        new_y = random.randrange(-250, 250, 5)
        self.goto(300,new_y)
