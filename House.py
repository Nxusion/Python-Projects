import turtle as t

t.bgcolor("cyan")
t.width(5)

t.penup()
t.rt(180)
t.fd(600)
t.lt(180)
t.pendown()

t.hideturtle()


def square():
    for i in range(4):
        t.fd(100)
        t.rt(90)


def triangle():
    for i in range(3):
        t.fd(100)
        t.lt(120)


def create_house():
    t.begin_fill()
    t.color("blue")
    t.pendown()

    square()

    t.end_fill()

    t.begin_fill()
    t.color("orange")

    triangle()

    t.end_fill()

    t.penup()
    t.color("blue")
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)


for x in range(8):
    create_house()

t.exitonclick()
