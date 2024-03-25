from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My pong game")


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

revert = 2

left_score = 0
right_score = 0

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)

    #Colission with borders Y
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    #Colission with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        score.refresh_left()
        ball.reset_position()
    if ball.xcor() < -380:
        score.refresh_right()
        ball.reset_position()


screen.exitonclick()