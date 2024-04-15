from turtle import Turtle



class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.setpos(position)
        self.color("light blue")
        self.shapesize(stretch_wid=1, stretch_len=5)

    def move_left(self):
            new_x = self.xcor() - 30
            self.goto(y=self.ycor(), x=new_x)

    def move_right(self):
            new_x = self.xcor() + 30
            self.goto(y=self.ycor(), x=new_x)

    def dragging(self, x):
        self.ondrag(None)
        self.setheading(self.towards(x))
        self.goto(x)
        self.ondrag(self.dragging)


