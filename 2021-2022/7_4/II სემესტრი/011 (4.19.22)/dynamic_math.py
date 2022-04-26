import turtle

t = turtle.Turtle()

ypos = 220

t.ht()
turtle.ht()


def dynamic_math(x, y, op, col):
  global ypos

  display = f"Bad operator '{op}'"

  t.pencolor(col)
  t.pu()
  t.goto(0, ypos)
  t.pd()

  ypos -= 80

  try:
    if op == '+': display = f"{x} + {y} = {x + y}"
    elif op == '-': display = f"{x} - {y} = {x - y}"
    elif op == '*': display = f"{x} * {y} = {x * y}"
    elif op == '/': display = f"{x} / {y} = {(x / y):.2f}"
    elif op == '//': display = f"{x} // {y} = {x // y}"
    elif op == '%': display = f"{x} % {y} = {x % y}"

    t.write(display, font=("georgia", 45, 'bold'), align='center')
  except ZeroDivisionError:
    display = f"{x} {op} {y} = {'Division by ZERO!'}"
    t.write(display, font=("georgia", 45, 'bold'), align='center')