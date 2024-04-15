from turtle import Screen

from paddle import Paddle
from Ball import Ball
from wall_tiles import Wall
from scoreboard import Scoreboard
import time
import random


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -200))
scoreboard = Scoreboard()
ball = Ball()
wall = Wall()

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

game_is_on = True
speed = 0.1

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with walls
    if ball.ycor() >= 285:
        ball.vertical_wall_bounce()

    if ball.xcor() > 385 or ball.xcor() < -385:
        ball.horizontal_wall_bounce()

    if ball.ycor() < - 290:
        game_is_on = False
        scoreboard.update_highscore()

    # Detect collision with paddle
    if ball.distance(paddle) < 40 and ball.ycor() > paddle.ycor() and ball.y_move < 0:
        ball.paddle_bounce()
        # add some slight randomness to bounce
        ball.x_move = random.uniform(-7, 7)

    # Detect collision with point bricks
    for segment in wall.wall_segments:
        if ball.distance(segment) < 30:
            segment.hit()
            ball.wall_segment_bounce()
            # add some slight randomness to bounce
            ball.x_move = random.uniform(-7, 7)
            wall.wall_segments.remove(segment)
            scoreboard.score += segment.value
            scoreboard.update_scoreboard()

    # Game completed if all point bricks hit
    if len(wall.wall_segments) == 0:
        game_is_on = False
        scoreboard.update_highscore()

    if not game_is_on:
        scoreboard.game_over()


screen.exitonclick()
