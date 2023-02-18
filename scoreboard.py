from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 80, 'normal')

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(position)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """ This function updates the scoreboard entry but without cleaning the previous value, see increase_score() for the full scoreboard update function. """
        self.write(arg=self.score, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """ Updating the user's score every time the food is eaten """
        self.score += 1
        self.clear()
        self.update_scoreboard()