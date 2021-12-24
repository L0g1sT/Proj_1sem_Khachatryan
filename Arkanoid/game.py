
import random
import pgzrun

TITLE = "Arkanoid"
WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

paddle = Actor("paddle.png")
paddle.x = 400
paddle.y = 575

ball = Actor("ball.png")
ball.x = 400
ball.y = 535.5

ball_x_speed = 3
ball_y_speed = 3

bars_list = []
score = 0
coloured_box_list = ["brickbg.png", "brickgg.png", "brickpr.png"]
x = 120
y = 100


def draw():
    screen.blit("background.png", (0, 0))
    paddle.draw()
    ball.draw()
    for bar in bars_list:
        bar.draw()


def place_bars(x, y, image):
    bar_x = x
    bar_y = y
    for i in range(9):
        bar = Actor(image)
        bar.x = bar_x
        bar.y = bar_y
        bar_x += 70
        bars_list.append(bar)


def update():
    global ball_x_speed, ball_y_speed
    if keyboard.left:
        paddle.x = paddle.x - 5
    if keyboard.right:
        paddle.x = paddle.x + 5


    update_ball()
    global score
    for bar in bars_list:
        if ball.colliderect(bar):
            bars_list.remove(bar)
            ball_y_speed *= -1
            score += 1
            print("Ваши очки: ", score)

    if paddle.colliderect(ball):
        ball_y_speed *= -1
        rand = random.randint(0, 1)
        if rand:
            ball_x_speed *= -1

    if paddle.x >= WIDTH - 40:
        paddle.x = paddle.x - 5
    if paddle.x <= 40:
        paddle.x = paddle.x + 5


def update_ball():
    global ball_x_speed, ball_y_speed
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed
    if (ball.x >= WIDTH - 15) or (ball.x <= 15):
        ball_x_speed *= -1
    if (ball.y <= 15):
        ball_y_speed *= -1
    if (ball.y >= HEIGHT):
        ball.x = 400
        ball.y = 535.5
        paddle.x = 400
        paddle.y = 575
        x = 120
        y = 100
        bars_list.clear()
        for i in range(3):
            place_bars(x, y, coloured_box_list[i])
            y += 50


for coloured_box in coloured_box_list:
    place_bars(x, y, coloured_box)
    y += 50

pgzrun.go()

