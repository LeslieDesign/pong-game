from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "6")
screen.onkey(r_paddle.go_down, "3")
screen.onkey(l_paddle.go_up, "4")
screen.onkey(l_paddle.go_down, "1")


game_is_on = True
while game_is_on:
    screen.update()




screen.exitonclick()