import turtle as t

t.bgcolor("blue")
t.width(10)
t.color("white")
t.pencolor("white")
t.hideturtle()


def square():
    for x in range(4):
        t.fd(100)
        t.rt(90)


def square2():
    for x in range(4):
        t.fd(100)
        t.lt(90)

def spacing():
    t.penup()
    t.fd(100)
    t.pendown()


square()
spacing()
square()
spacing()
square()

t.fd(50)
t.lt(90)

square2()

t.lt(90)
t.fd(100)

square()

t.rt(90)
t.fd(100)
t.rt(90)
t.fd(-50)

square2()

t.exitonclick()
