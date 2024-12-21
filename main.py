from turtle import Turtle, Screen
from box import Box
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)

r_box = Box((350, 0))
ball = Ball()
l_box = Box((-350, 0))

screen.onkey(r_box.go_up,"Up")
screen.onkey(l_box.go_up,"w")
screen.onkey(r_box.go_down,"Down")
screen.onkey(l_box.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()

    # Detect collision with ball
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_box) < 50 and ball.xcor() > 320 or ball.distance(l_box) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 370 :
        ball.reset_position()
        ball.bounce_x()
    if ball.xcor() < -370:
        ball.reset_position()
        ball.bounce_x()





screen.exitonclick()