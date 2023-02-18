from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """ This function is responsible for making the ball move by incrementing the x,y coordinates """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """ This function is responsible for decreasing the y-axis when the top and bottom walls are touched. """ 
        self.y_move *= -1

    def bounce_x(self):
        """ This function is responsible for decreasing the x-axis and increasing the ball speed when the paddles are touched. """
        self.x_move *= -1
        self.move_speed *=  0.9

    def reset_position(self):
        """ This function is responsible for restoring the position of the ball after it has ended up out of the field, restarting it by pointing in the opposite direction to where it ended up the previous time, and restores the move_speed to the initial value. """ 
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1