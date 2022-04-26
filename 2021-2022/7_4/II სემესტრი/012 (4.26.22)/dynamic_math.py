import turtle

t = turtle.Turtle()

t.ht()
turtle.ht()

ypos = 220


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

    t.write(display, align='center', font=("georgia", 45, 'bold'))
  except ZeroDivisionError:
    display = f"{x} {op} {y} = {'Division by Zero'}"
    t.write(display, align='center', font=("georgia", 45, 'bold'))
  except TypeError:
    t.pencolor('red')
    display = f"Input bad data for {x} and {y}"
    t.write(display, align='center', font=("georgia", 45, 'bold'))