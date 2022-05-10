import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("print a table")
turtle.setup(800, 500)
turtle.bgcolor("lightyellow")

t.ht()
turtle.ht()

a1, b1 = 1, 2
a2, b2 = 2, 3
a3, b3 = 3, 4
a4, b4 = 4, 5
a5, b5 = 5, 6
a6, b6 = 6, 7
a7, b7 = 7, 8
a8, b8 = 8, 9

w = 20
display = f"{'a':<{w}}{'b':<{w}}{'a ** b'}\n"\
          f"{a1:<{w}}{b1:<{w}}{a1 ** b1}\n"\
          f"{a2:<{w}}{b2:<{w}}{a2 ** b2}\n"\
          f"{a3:<{w}}{b3:<{w}}{a3 ** b3}\n"\
          f"{a4:<{w}}{b4:<{w}}{a4 ** b4}\n"\
          f"{a5:<{w}}{b5:<{w}}{a5 ** b5}\n"\
          f"{b6:<{w}}{b6:<{w}}{b6 ** b6}\n"\
          f"{a7:<{w}}{b7:<{w}}{a7 ** b7}\n"\
          f"{a8:<{w}}{b8:<{w}}{a8 ** b8}\n"

t.pencolor('darkred')
t.pu()
t.goto(0, -100)
t.pd()

t.write(display, align='center', font=("calibri", 15, 'bold'))


# =====================
turtle.exitonclick()