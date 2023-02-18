from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#General screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
#tracer to avoid initial animations
screen.tracer(0)

#Paddle
left_paddle = Paddle(position=(-350, 0))
right_paddle = Paddle(position=(350, 0))
#Paddles movements
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.listen()

#Ball
ball = Ball()

#Scoreboard
left_player_score = Scoreboard(position=(-100, 200))
right_player_score = Scoreboard(position=(100, 200))

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    #update the screen to avoid initial animations
    screen.update()

    #starting moving the ball
    ball.move()

    #Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses and increase left_player_score
    if ball.xcor() > 380:
        ball.reset_position()
        left_player_score.increase_score()

    #Detect L paddle misses and increase right_player_score
    if ball.xcor() < -380:
        ball.reset_position()
        right_player_score.increase_score()

screen.mainloop()
screen.exitonclick()