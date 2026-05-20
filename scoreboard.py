from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # Sol skor - Y koordinatını biraz düşürdük (180)
        self.goto(-100, 180) 
        self.write(self.l_score, align="center", font=("Courier", 60, "bold"))
        # Sağ skor
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 60, "bold"))
        
        # Ekranın yazıyı çizdiğinden emin oluyoruz
        if self.screen:
            self.screen.update()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()