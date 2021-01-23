from turtle import Turtle

FONT = ("Trattatello", 22, "normal")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("darkred")
        self.up()
        self.ht()
        self.goto(0, 260)
        self.speed("fastest")
        self.score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"TOTAL KILLS: {self.score}", False, ALIGN, FONT)

    def add_score(self, points):
        self.score += points
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, ALIGN, FONT)
