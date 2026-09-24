from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.pencolor("black")
        self.write_score()

    def increase_score(self):
        self.level += 1
        self.write_score()

    def write_score(self):
        self.write(f"Level: {self.level}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
