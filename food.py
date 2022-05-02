from turtle import *
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.speed("fast")
        self.color("blue")
        self.shapesize(0.5)
        self.refresh()

    def refresh(self):
        x = random.randint(-280,280)
        y = random.randint(-280,265)
        self.setposition(x,y)