from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.pu()
        self.balls = 5
        self.right(randint(-45, 45))

    def bounce(self, angle):
        self.setheading(180 - self.heading() - angle)

    def lost(self, side):
        self.balls -= 1
        self.refresh(side)

    def refresh(self, side="left"):
        self.home()
        if side == 'left':
            self.setheading(180)
        elif side == 'right':
            pass
        self.right(randint(-45, 45))
