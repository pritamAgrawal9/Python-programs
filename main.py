from turtle import Turtle, Screen
from box import Box
from ball import Ball


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)

r_box = Box((350, 0))
l_box = Box((-350, 0))


screen.onkey(r_box.go_up,"Up")
screen.onkey(l_box.go_up,"w")
screen.onkey(r_box.go_down,"Down")
screen.onkey(l_box.go_down,"s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()