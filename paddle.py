from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.goto(position)

    def move_up(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + 10)

    def move_down(self):
        if self.ycor() > -250:
            self.sety(self.ycor() - 10)
