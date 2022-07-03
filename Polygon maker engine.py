import tkinter
from tkinter import *
import turtle as t


def setup():
    print("Generating polygon...")
    t.reset()
    t.penup()
    t.lt(180)
    t.fd(150)
    t.rt(90)
    t.fd(-150)
    t.rt(90)
    t.pendown()
    t.bgcolor("blue")
    t.pencolor("light blue")
    t.fillcolor("cyan")
    section_a = t.textinput("Step 1 - Length", "How many pixels should the polygon have?")
    section_b = t.textinput("Step 2 - Sides", "How many sides do your polygon to have?")
    length = section_a
    sides = section_b
    a = int(length)
    b = int(sides)

    t.begin_fill()

    for x in range(b):
        t.fd(a)
        t.lt(360 / b)

    t.end_fill()

    tkinter.messagebox.showinfo("All done", "Drawing complete.", icon="info")


window = Tk()

window.title("TextBox Input")
window.geometry('300x150')
Label(window, text="Polygon maker 1.0", font=('Open Sans Bold', 20)).pack(pady=20)

length_text = Label(window, text="Click create new to start")
initial_command = Button(text="Create new", command=setup)

length_text.pack()
initial_command.pack()

t.exitonclick()
