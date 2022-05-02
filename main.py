import time
import turtle

from food import Food
from scoreboard import ScoreBoard
from snake import *

screen= Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

game = True

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.my_snake[0].distance(food)<14:
        food.refresh()
        snake.extend()
        scoreboard.update()
    if snake.my_snake[0].xcor()>280 or snake.my_snake[0].xcor()<-285 or snake.my_snake[0].ycor()>270 or snake.my_snake[0].ycor()<-280:
        game = False
        scoreboard.game_over()
    for segment in snake.my_snake[1:]:
        if snake.my_snake[0].distance(segment)<10:
            game = False
            scoreboard.game_over()
screen.exitonclick()