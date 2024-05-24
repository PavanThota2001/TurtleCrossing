COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10
from turtle import Turtle
import random
import time


class CarManager:
    def __init__(self):
        self.cars = []



    def segment(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new = Turtle("square")
            new.shapesize(stretch_wid=1, stretch_len=3)
            new.color(random.choice(COLORS))
            new.penup()
            new.goto(320, random.randint(-250, 250))
            self.cars.append(new)

    def move(self):
        for car in self.cars:
            car.backward(MOVE_INCREMENT)



