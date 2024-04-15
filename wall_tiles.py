from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.is_hit = False
        self.penup()
        self.color('white')
        self.shape("square")
        self.speed("fastest")
        self.value = 10
        self.shapesize(stretch_len=2, stretch_wid=1)
        if self.is_hit:
            self.hit()

    def hit(self):
        self.penup()
        self.setposition(380, 380)


class Wall:
    def __init__(self):
        self.wall_segments = []
        self.create_wall()

    def create_wall(self):
        x_cor = -370
        for line in range(17):
            line = Line()
            line.color("red")
            line.goto(x=x_cor, y=-25)
            line.value = 10
            self.wall_segments.append(line)
            x_cor += 46
        x_cor = -370
        for line in range(17):
            line = Line()
            line.color("red")
            line.goto(x=x_cor, y=0)
            line.value = 10
            self.wall_segments.append(line)
            x_cor += 46
        x_cor = -370
        for line in range(17):
            line = Line()
            line.color("yellow")
            line.goto(x=x_cor, y=25)
            line.value = 13
            self.wall_segments.append(line)
            x_cor += 46
        x_cor = -370
        for line in range(17):
            line = Line()
            line.color("yellow")
            line.goto(x=x_cor, y=50)
            line.value = 13
            self.wall_segments.append(line)
            x_cor += 46
        x_cor = -370
        for line in range(17):

            line = Line()
            line.value = 24
            line.color("green")
            line.goto(x=x_cor, y=75)
            self.wall_segments.append(line)
            x_cor += 46
        x_cor = -370
        for line in range(17):
            line = Line()
            line.value = 24
            line.color("green")
            line.goto(x=x_cor, y=100)
            self.wall_segments.append(line)
            x_cor += 46
        x_cor = -370
        for line in range(17):
            line = Line()
            line.color("orange")
            line.value = 31
            line.goto(x=x_cor, y=125)
            self.wall_segments.append(line)
            x_cor += 46
        x_cor = -370
        for line in range(17):
            line = Line()
            line.value = 31
            line.color("orange")
            line.goto(x=x_cor, y=150)
            self.wall_segments.append(line)
            x_cor += 46
