#!/usr/bin/env python

import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.tracer(0)

score = turtle.Turtle()
score.ht()
score.pu()
score.color("yellow")

pad1 = Paddle((460, 0))
pad2 = Paddle((-460, 0))
players = {"player1": 0, "player2": 0}
ball = Ball()
screen.update()
screen.listen()
screen.onkey(turtle.bye, "Escape")
screen.onkey(pad1.move_up, "Up")
screen.onkey(pad1.move_down, "Down")
screen.onkeypress(pad2.move_up, "w")
screen.onkeypress(pad2.move_down, "s")

goon = True

while goon:
    screen.update()
    score.clear()
    score.goto(-480, 260)
    score.write(f"Player 1: {players['player1']}", align="left", font=("Neuropolitical", 10, "normal"))
    score. goto(360, 260)
    score.write(f"Player 2: {players['player2']}", align="left", font=("Neuropolitical", 10, 'normal'))
    if ball.balls == 0:
        score.home()
        score.write("GAME OVER!", align="center", font=("Neuropolitical", 20, "normal"))
        goon = False
    ball.forward(10)
    sleep(0.04)
    if ball.xcor() > 470:
        players["player1"] += 1
        ball.lost(side="left")
    elif ball.ycor() > 280:
        ball.bounce(-180)
    elif ball.ycor() < -280:
        ball.bounce(180)
    elif ball.xcor() > 440 and ball.distance(pad1) < 50:
        ball.bounce(ball.distance(pad1) / 10)
    elif ball.xcor() < -440 and ball.distance(pad2) < 50:
        ball.bounce(0)
    elif ball.xcor() < -470:
        players["player2"] += 1
        ball.lost(side="right")

turtle.mainloop()
