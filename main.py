import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
cars = CarManager()
score_update = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forward,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.car_movement()

    if player.ycor() == 280:
        cars.level_up_speed()
        player.cross_again()
        score_update.increase_score()

    for car in cars.all_cars:
        if car.distance(player) < 25:
            score_update.game_result()
            game_is_on = False

screen.exitonclick()