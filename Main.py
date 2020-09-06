# Virtual Pong
# Dan MacDonald


import turtle

dow = turtle.Screen()
dow.title("Dan's Virtual Pong")
dow.setup(width=800, height=600)
dow.bgcolor('black')
dow.tracer(0)

# Score
s_a = 0
s_b = 0

# Player 1
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape('square')
pad_a.color('lime green')
pad_a.shapesize(stretch_wid=6, stretch_len=1)
pad_a.penup()
pad_a.goto(-350, 0)

# Player 2
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape('square')
pad_b.color('lime green')
pad_b.shapesize(stretch_wid=6, stretch_len=1)
pad_b.penup()
pad_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('lime green')
ball.penup()
ball.goto(0, 0)
ball.dx = .15
ball.dy = .15


def pad_a_up():
    y = pad_a.ycor()
    y += 30
    pad_a.sety(y)


def pad_a_down():
    y = pad_a.ycor()
    y += -30
    pad_a.sety(y)


def pad_b_up():
    y = pad_b.ycor()
    y += 30
    pad_b.sety(y)


def pad_b_down():
    y = pad_b.ycor()
    y += -30
    pad_b.sety(y)


# Key binds
dow.listen()
dow.onkeypress(pad_a_up, "w")
dow.onkeypress(pad_a_down, "s")
dow.onkeypress(pad_b_up, "Up")
dow.onkeypress(pad_b_down, "Down")

# Scoreboard
p = turtle.Turtle()
p.speed(0)
p.color('lime green')
p.penup()
p.hideturtle()
p.goto(0, 260)


# Main game
while True:
    dow.update()


    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        s_a += 1
        p.clear()
        p.write('Player1: {} Player2: {}'.format(s_a, s_b), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        s_b += 1
        p.clear()
        p.write('Player1: {} Player2: {}'.format(s_a, s_b), align='center', font=('Courier', 24, 'normal'))

    # Hitting the ball

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad_b.ycor() + 40 and ball.ycor() > pad_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad_a.ycor() + 40 and ball.ycor() > pad_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1








