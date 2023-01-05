from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.penup()
        self.move()

    def move(self):
        y_cord=random.randint(-280, 280)
        x_cord=random.randint(-280, 280)
        self.goto(x_cord, y_cord)