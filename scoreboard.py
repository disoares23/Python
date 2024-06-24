from turtle import Turtle
FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.setposition(-240, 260)
        self.level = 0
        self.write(f"Level: {self.level}",align="center", font=FONT)


    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)


    def end_score(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over! You've reached to level: {self.level}", align="center", font=FONT)

