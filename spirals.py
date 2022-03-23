"""
Author: Huaqing Sun (Annabelle Sun)
Date: 20220318
File Name: spirals.py
The file is to create a flower pic
with python turtle
"""
import turtle as t


def spirals():
    """
    a function to draw spirals with python turtle
    return: none, the screen will show pics
    """
    s = t.getscreen()
    # t = turtle.Turtle()
    t.title("Annabelle's Turtle Program")
    s.bgcolor('white')
    t.pensize(2)
    t.speed(50000000)
    t.home()

    for i in range(36):
        t.pencolor('#F473B9')
        t.circle(100)
        t.left(10)
    t.home()

    for i in range(255 * 1):
        t.fd(50 + i)
        t.rt(91)
        t.pencolor("#FFBDE6")

    t.home()
    for i in range(300):
        t.circle(190 - i, 90)
        t.left(90)
        t.circle(190 - i, 90)
        t.left(18)
        t.pencolor('#FFDDEE')

    t.hideturtle()
    t.up()
    t.mainloop()
    t.done()


def main():
    spirals()


if __name__ == '__main__':
    main()
