from turtle import *


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.sety(270)
        self.color("white")
        self.write(f"score = {self.score}", False, "center", ("arial", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, "center", ("arial", 15, "normal"))



    def update(self):
        self.score += 1
        self.clear()
        self.write(f"score = {self.score}", False, "center", ("arial", 15, "normal"))
