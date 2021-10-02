from turtle import Turtle

SCORE = 0
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=("Courier", 24, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
