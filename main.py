import time
from turtle import Screen

import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
NEW_CAR_MOVE_SPEED = 0.1

cars = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

myturtle = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(myturtle.move, "Up")

game_is_on = True
new_car_cue = 0
while game_is_on:
    print(f"Cars left: {len(cars)}")
    screen.update()
    if new_car_cue%6 == 0:
        car = CarManager()
        car.move_speed = NEW_CAR_MOVE_SPEED
        cars.append(car)
    new_car_cue += 1
    time.sleep(cars[0].move_speed)
    for car in cars:
        car.drive()
        if car.xcor()<-320:
            car.clear()
            cars.remove(car)
        if myturtle.distance(car)<10:
            scoreboard.game_over()
            game_is_on = False
    if myturtle.ycor() > player.FINISH_LINE_Y:
        NEW_CAR_MOVE_SPEED *= 0.8
        scoreboard.clear()
        scoreboard.increase_score()
        myturtle.reset_position()

screen.exitonclick()