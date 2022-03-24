from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.speed(0)

    def increase_score(self):
        self.score += 1

    def display_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score : {self.high_score}", align="center", font=("Courier", 12, "normal"))

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt",mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.display_score()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game Over.", align="center", font=("Courier", 12, "normal"))