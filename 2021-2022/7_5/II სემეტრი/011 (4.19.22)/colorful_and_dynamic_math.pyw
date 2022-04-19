import turtle

ypos = 200


def dynamic_math(x ,y, op, col):
  global ypos

  t.pencolor(col)
  t.pu()
  t.goto(0, ypos)
  t.pd()

  ypos -= 90

  try:
    if op == '+': display = f"{x} + {y} = {x + y}"
    elif op == '-': display = f"{x} - {y} = {x - y}"
    elif op == '*': display = f"{x} * {y} = {x * y}"
    elif op == '/': display = f"{x} / {y} = {(x / y):.2f}"
    elif op == '//': display = f"{x} // {y} = {x // y}"
    elif op == '%': display = f"{x} % {y} = {x % y}"

    t.write(display, font=("georgia", 45, 'bold'), align='center')
  except ZeroDivisionError:
    t.write(display, font=("georgia", 45, 'bold'), align='center')



# =====> RUN PROGRAM <=====
s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Colorful and dynamic Math")
turtle.setup(width=1000, height=600)
turtle.bgcolor('lightyellow')

t.ht()
turtle.ht()

num1 = turtle.numinput("Input numbers", "First number:")
num2 = turtle.numinput("Input numbers", "Second number:")

dynamic_math(int(num1), int(num2), "+", 'red')
dynamic_math(int(num1), int(num2), "-", 'blue')
dynamic_math(int(num1), int(num2), "*", 'green')
dynamic_math(int(num1), int(num2), "/", 'salmon')
dynamic_math(int(num1), int(num2), "//", 'magenta')
dynamic_math(int(num1), int(num2), "%", 'darkviolet')


# =====================
turtle.exitonclick()