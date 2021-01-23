from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color("darkred")
        self.up()
        self.shape("turtle")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.respawn()

    def respawn(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)