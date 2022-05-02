import turtle
from turtle import *


class Snake:
    start = [(0, 0), (-20, 0), (-40, 0)]
    my_snake = []

    def __init__(self):
        for place in self.start:
            self.add_segment(place)

    def add_segment(self, position):
        tim = Turtle("square")
        tim.penup()
        tim.color("white")
        tim.goto(position)
        self.my_snake.append(tim)

    def extend(self):
        self.add_segment(self.my_snake[-1].pos())

    def move(self):
        for i in range(len(self.my_snake) - 1, 0, -1):
            self.my_snake[i].goto(self.my_snake[i - 1].xcor(), self.my_snake[i - 1].ycor())
        self.my_snake[0].forward(20)

    def up(self):
        self.my_snake[0].setheading(90)

    def down(self):
        self.my_snake[0].setheading(270)

    def left(self):
        self.my_snake[0].setheading(180)

    def right(self):
        self.my_snake[0].setheading(0)
