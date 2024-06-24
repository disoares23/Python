import random
import pygame
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import music_player


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
FONT = ("Courier", 12, "normal")

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True

while game_is_on:
    speed = 1
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 27:
            game_is_on = False
            scoreboard.end_score()
            music_player.play_game_over()


    # Detect on finish line
    if player.ycor() > 290:
        player.reset_position()
        scoreboard.update_level()
        car_manager.level_up()
        music_player.play_level_up()


screen.exitonclick()

