from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.highscore=int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(0,260)
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("Courier", 24, "normal"))

    def update_highscore(self):
        if self.score > self.highscore:
            self.highscore=self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_score()

    def refresh(self):
        self.score+=1
        self.update_score()
    
    