import time
from turtle import Screen
from player import Player
from TurtleCrossing.car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
car_manage = CarManager()
screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")
game_is_on = True
i = 0.0
while game_is_on:
    screen.update()
    time.sleep(0.1 - i)
    car_manage.segment()
    car_manage.move()
    if player.ycor() >= 290:
        scoreboard.update_score()
        player.base()
        i += 0.02
    for car in car_manage.cars:
        if player.distance(car) < 35:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
screen.exitonclick()




