import time
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("light blue")
        self.penup()
        self.setposition(0, -160)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.07


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def horizontal_wall_bounce(self):
        self.x_move *= -1

    def vertical_wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.99


    def wall_segment_bounce(self):
        self.y_move *= -1
        self.x_move *= -1
