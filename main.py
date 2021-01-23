from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# some config
width = 600
height = 600
speed = 20
sleep = 0.1
snake_color = "white"

screen = Screen()
screen.setup(width=width, height=height)
screen.bgcolor("black")
screen.title("Snake Eternal")
screen.tracer(0)
game_over = False

snake = Snake(color=snake_color)
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

while not game_over:
    screen.update()
    time.sleep(sleep)
    snake.move(speed)

    if snake.head.distance(food) < 15:
        scoreboard.add_score(1)
        food.respawn()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        game_over = True
        scoreboard.game_over()

    for pcs in snake.pieces[2:]:
        if snake.head.distance(pcs) < 10:
            game_over = True
            scoreboard.game_over()

screen.exitonclick()
