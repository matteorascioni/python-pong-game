from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    # Handling the paddles onkey movements
    def go_up(self):
        """ This function is responsible for managing the upward movement of the paddle by increasing the Y coordinate. """
        new_y = self.ycor() + 20
        return self.goto(self.xcor(), new_y)
            
    def go_down(self):
        """ This function is responsible for managing the downward movement of the paddle by decreasing the Y coordinate. """
        new_y = self.ycor() - 20
        return self.goto(self.xcor(), new_y)