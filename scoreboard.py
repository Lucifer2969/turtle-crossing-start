from turtle import Turtle
FONT = ("Courier", 20, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.penup()
        self.color("black")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-270, 270)
        self.write(arg= f"Level : {self.count}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.count += 1
        self.update_scoreboard()

    def game_result(self):
        self.goto(-50,0)
        self.write(arg=f"Game Over", align=ALIGNMENT, font=FONT)