from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

game_is_on = True

def game_stop():
    global game_is_on
    game_is_on = False

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


screen.update()
screen.listen()
screen.onkey(game_stop, "c")

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detects collision with the food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.clear()
        score.increase_score()
        snake.extend()

    #detects collision with the wall
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -290:
        game_stop()
        score.game_over()
    screen.onkey(game_stop, "c")

    tail = snake.segments[1:]
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()