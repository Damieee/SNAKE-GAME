from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

screen=Screen()
my_snake=Snake()

scoreboard=Scoreboard()
screen.tracer(0)
food=Food()
#this sets screen size
screen.setup(height=600, width=600)

#this sets the background colour
screen.bgcolor("black")

#this sets title of game at heading
screen.title("Damilare's Snake Game")



screen.listen()

screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    my_snake.move_snake()
    if my_snake.head.distance(food)<15:
        food.move()
        my_snake.extend()
        scoreboard.refresh()

    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        scoreboard.update_highscore()
        my_snake.reset()

    for segments in my_snake.segments[1:]:
        if my_snake.head.distance(segments)<10:
            scoreboard.update_highscore()
            my_snake.reset()
        
screen.exitonclick()