FONT = ("Courier", 24, "normal")
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-240, 270)
        self.write(f"Level: {self.score}", align="center", font=('Arial', 20, 'normal'))
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", align="center", font=('Arial', 20, 'normal'))
    def game_over(self):
        self.color("black")
        self.goto(0, 0)
        self.write("Game Over", align="center", font=('Arial', 20, 'normal'))

