import turtle
import random


def run_game():
    turtle.resetscreen()
    turtle.delay(0)

    # score and lives
    score = 0
    lives = 3

    # Draw screen
    screen = turtle.Screen()
    screen.title("My Breakout")
    screen.bgcolor("black")
    screen.setup(width=600, height=800)
    screen.tracer(0)

    # Draw paddle
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=0.5, stretch_len=2)
    paddle.penup()
    paddle.goto(0, -350)

    # draw ball
    ball = turtle.Turtle()
    ball.speed(1)
    ball.shape("circle")
    ball.color("white")
    ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
    ball.penup()
    ball.goto(0, 0)
    ball.dx = random.choice((-1, -0.7, -0.5, 0.5, 0.7, 1))
    ball.dy = random.choice((-1, -0.7, 0.7, 1))

    # Draw blocks
    blocks_x = [-263, -198, -133, -68, -3, 62, 127, 192, 257]
    blocks_y = [260, 240, 220, 200, 180]
    block_list = []
    colors = ['red', 'orange', 'green', 'lightgreen', 'yellow']
    color_index = 0

    for i in blocks_x:
        for j in blocks_y:
            block = turtle.Turtle()
            block.speed(0)
            block.shape("square")
            block.color(colors[color_index])
            block.shapesize(stretch_wid=0.5, stretch_len=3)
            block.penup()
            block.goto(i, j)
            block_list.append(block)
            color_index += 1
        color_index = 0

    block_count = len(block_list)

    # head-up display
    hud = turtle.Turtle()
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(0, 320)
    hud.write(f"LIVES: {lives}\n", align="center", font=("Courier", 18, "normal"))
    hud.write(f"SCORE: {score}", align="center", font=("Courier", 18, "normal"))

    def paddle_right():
        if paddle.xcor() < 270:
            paddle.setx(paddle.xcor() + 30)

    def paddle_left():
        if paddle.xcor() > -270:
            paddle.setx(paddle.xcor() - 30)

    def paddle_collision():
        if ball.ycor() == -340:
            if (ball.xcor() > paddle.xcor() - 30) and (ball.xcor() < paddle.xcor() + 30):
                ball.dy *= -1

    # keyboard
    screen.listen()
    screen.onkeypress(paddle_right, "d")
    screen.onkeypress(paddle_left, "a")

    while block_count > 0 and lives >= 0:
        screen.update()

        # ball movement
        ball.setx(ball.xcor() - ball.dx)
        ball.sety(ball.ycor() - ball.dy)

        paddle_collision()

        # collision with the right wall
        if ball.xcor() > 290:
            ball.dx *= -1

        # collision with left wall
        if ball.xcor() < -290:
            ball.dx *= -1

        # collision with upper wall
        if ball.ycor() > 390:
            ball.dy *= -1

        # collision with bottom wall
        if ball.ycor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            lives -= 1
            hud.clear()
            hud.write(f"LIVES: {lives}\n", align="center", font=("Courier", 18, "normal"))
            hud.write(f"SCORE: {score}", align="center", font=("Courier", 18, "normal"))

        # collision with the paddle
        if ball.xcor() < -330 and paddle.xcor() + 50 > ball.ycor() > paddle.xcor() - 50:
            ball.dx *= -1

        for i in block_list:
            if (ball.xcor() >= i.xcor()-30) and (ball.xcor() <= i.xcor()+30):
                if (ball.ycor()+5 >= i.ycor()-10) and (ball.ycor()-5 <= i.ycor()+10):
                    if (i.ycor()-10 - ball.ycor()+5) >= 0 or (i.ycor()+10 - ball.ycor()-5) >= 0:
                        ball.dy *= -1
                    elif (i.xcor()-30 - ball.xcor()) >= 0 or (i.xcor()+30 - ball.xcor()) >= 0:
                        ball.dx *= -1
                    else:
                        ball.dy *= -1
                        ball.dx *= -1
                    i.goto(1000, 1000)
                    score += 1
                    hud.clear()
                    hud.write(f"LIVES: {lives}\n", align="center", font=("Courier", 18, "normal"))
                    hud.write(f"SCORE: {score}", align="center", font=("Courier", 18, "normal"))
                    block_count -= 1

    ball.reset()
    for i in block_list:
        i.reset()
    paddle.reset()
    hud.clear()
    hud.color("red")
    hud.goto(0, 70)
    hud.write("GAME OVER", align="center", font=("Courier", 40, "normal"))
    hud.goto(0, 10)
    hud.color("white")
    hud.write(f"SCORE: {score}", align="center", font=("Courier", 24, "normal"))
    hud.goto(0, -50)
    hud.write("Press Enter to play again", align="center", font=("Courier", 18, "normal"))


run_game()

turtle.onkeypress(run_game, "Return")
turtle.done()
