import sys
sys.dont_write_bytecode = True

# Mevcut importların bundan sonra gelsin:
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Ekran Ayarları
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong - Q/E Hız Kontrolü")
screen.tracer(0)

# Objeleri Başlatma
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Kontrolleri Dinleme
screen.listen()

# Raket Hareketleri
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Hız Kontrolleri (YENİ KISAYOLLAR)
screen.onkey(ball.fast_up, "q")    # Q tuşu ile hızlanma
screen.onkey(ball.slow_down, "e")  # E tuşu ile yavaşlama

# Oyun Döngüsü
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Üst/Alt Duvar Çarpışması
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Raketle Çarpışma
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Skor Durumları
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()