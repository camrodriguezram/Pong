from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_right = 0
        self.score_left = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0,250)
        self.write(f"{self.score_left} : {self.score_right} ",False, align="center",font=("Courier",15, "normal"))


    def update(self):
        self.clear()
        self.write(f"{self.score_left} : {self.score_right} ", False, align="center", font=("Verdana", 15, "normal"))

    def refresh_left(self):
        self.score_left += 1
        self.update()

    def refresh_right(self):
        self.score_right += 1
        self.update()

