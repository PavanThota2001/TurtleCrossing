STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.down()
        self.left()
        self.right()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.base()


    def base(self):

        self.setheading(90)
        self.goto(0, -280)
    def up(self):
        self.penup()
        self.setheading(UP)
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def down(self):
        self.setheading(DOWN)
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
    def left(self):
        self.setheading(LEFT)
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
    def right(self):
        self.setheading(RIGHT)
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())




