import turtle

t = turtle.Turtle()

t.ht()
turtle.ht()

ypos = 220


def dynamic_math(x, y, op, col):
  global ypos

  display = f"{x} {op} {y} = Bad operator '{op}'"

  t.pencolor(col)
  t.pu()
  t.goto(x=0, y=ypos)
  t.pd()

  ypos -= 80

  try:
    if op == '+': display = f"{x} {op} {y} = {x + y}"
    elif op == '-': display = f"{x} {op} {y} = {x - y}"
    elif op == '*': display = f"{x} {op} {y} = {x * y}"
    elif op == '/': display = f"{x} {op} {y} = {(x / y):.2f}"
    elif op == '//': display = f"{x} {op} {y} = {x // y}"
    elif op == '%': display = f"{x} {op} {y} = {x % y}"

    t.write(display, align='center', font=("georgia", 45, 'bold'))
  except ZeroDivisionError:
    display = f"{x} {op} {y} = {'Division by ZERO!'}"
    t.write(display, align='center', font=("georgia", 45, 'bold'))