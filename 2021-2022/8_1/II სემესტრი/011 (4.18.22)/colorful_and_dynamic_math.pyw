import turtle

ypos = 200


def dynamic_math(x, y, op, col):
  global ypos

  display = ''

  t.pencolor(col)
  t.pu()
  t.goto(0, ypos)
  t.pd()

  ypos -= 90

  if op == '+': display = f"{x} {op} {y} = {x + y}"
  elif op == '-': display = f"{x} {op} {y} = {x - y}"
  elif op == '*': display = f"{x} {op} {y} = {x * y}"
  elif op == '/': display = f"{x} {op} {y} = {(x / y):.2f}"
  elif op == '//': display = f"{x} {op} {y} = {x // y}"
  elif op == '%': display = f"{x} {op} {y} = {x % y}"

  t.write(display, font=("georgia", 45, 'bold'), align='center')


# =====> RUN PROGRAM <=====
s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Colorful and dynamic Math")
turtle.setup(width=1000, height=600)
turtle.bgcolor("lightyellow")

t.ht()
turtle.ht()

num1 = int(turtle.numinput("Input numbers", "First number:"))
num2 = int(turtle.numinput("Input numbers", "Second number:"))

dynamic_math(num1, num2, '+', 'red')
dynamic_math(num1, num2, '-', 'blue')
dynamic_math(num1, num2, '*', 'green')
dynamic_math(num1, num2, '/', 'salmon')
dynamic_math(num1, num2, '//', 'magenta')
dynamic_math(num1, num2, '%', 'darkviolet')


# ===================
turtle.exitonclick()