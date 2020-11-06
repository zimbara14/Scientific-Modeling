import turtle
import time
import random

is_elastic = True
# if non elastic collision required, change is_elastic to False

screen = turtle.Screen()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 450
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("white")

pen = turtle.Pen()
pen.color("black")
pen.hideturtle()
pen.up()
pen.goto(0, 150)
pen.hideturtle()


class Ball(turtle.Turtle):
    def __init__(self, mass, velocity, x_start):
        super().__init__(shape="circle", visible=False)
        self.mass = mass
        self.x_start = x_start
        self.velocity = velocity
        self.shapesize(mass)
        self.radius = (mass * 10)
        self.color_list = ["red", "blue", "green", "yellow", "orange", "purple"]
        self.color(random.choice(self.color_list))
        self.up()
        self.goto(self.x_start, 0)
        self.down()
        self.showturtle()

    def move(self):
        self.up()
        self.goto(self.xcor() + self.velocity, self.ycor())
        if self.xcor() >= screen.window_width() / 2 - self.radius or self.xcor() <= -screen.window_width() / 2 + self.radius:
            self.velocity *= -1


ball1 = Ball(7, 8, -400)
ball2 = Ball(4, 0, 200)
pen.write("Parameters:\n\n", align='center', font=("Courier", 16, "bold"))
pen.write(
    f"m1: {ball1.mass}, V1: {ball1.velocity:.3f}, m2: {ball2.mass}, V2: {ball2.velocity:.3f}\n",
    align='center', font=("Courier", 12, "normal"))
count = 0
while True:
    time.sleep(0.01)
    screen.update()
    ball1.move()
    ball2.move()
    if abs((ball1.xcor() - ball2.xcor())) <= ball1.radius + ball2.radius:
        if is_elastic:
            ball1_new = ((ball1.mass - ball2.mass) * ball1.velocity + 2 * ball2.mass * ball2.velocity) / (
                    ball1.mass + ball2.mass)
            ball2_new = ((ball2.mass - ball1.mass) * ball2.velocity + 2 * ball1.mass * ball1.velocity) / (
                    ball1.mass + ball2.mass)
            ball1.velocity = ball1_new
            ball2.velocity = ball2_new
        else:
            ball_new = (ball1.mass * ball1.velocity + ball2.mass * ball2.velocity) / (ball1.mass + ball2.mass)
            ball1.velocity = ball_new
            ball2.velocity = ball_new
        if count < 1 and not is_elastic or is_elastic:
            pen.clear()
            pen.write("Parameters:\n\n", align='center', font=("Courier", 16, "bold"))
            pen.write(
                f"m1: {ball1.mass}, V1: {ball1.velocity:.3f}, m2: {ball2.mass}, V2: {ball2.velocity:.3f}\n",
                align='center', font=("Courier", 12, "normal"))
            count += 1
