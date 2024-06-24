from turtle import Turtle

import music_player

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.setposition(0, -280)

    def move_up(self):
        music_player.play_step()
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def player_position(self):
        actual_position = (self.xcor, self.ycor)

