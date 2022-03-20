from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.speed(0)

    def increase_score(self):
        self.score += 1

    def display_score(self):
        score = self.score
        self.write(arg=f"Score : {score}", align="center", font=("Courier", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over.", align="center", font=("Courier", 12, "normal"))