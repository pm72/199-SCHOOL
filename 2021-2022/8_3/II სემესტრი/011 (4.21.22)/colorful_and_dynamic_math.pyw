import turtle


def dynamic_math(x, y, op, col):
  t.pencolor(col)
  t.pu()
  t.goto(x=0, y=220)
  t.pd()

  # display = f"{x} + {y} = {x + y}"
  t.write('display', align='center', font=("georgia", 45, 'bold'))


# =====> RUN MAIN PROGRAMM <=====
s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("colorful and dynamic Math")
turtle.setup(width=1000, height=600)
turtle.bgcolor('lightyellow')

t.ht()
turtle.ht()

num1 = turtle.numinput(title="Input numbers", prompt="First number:")
num2 = turtle.numinput(title="Input numbers", prompt="Second number:")

dynamic_math(num1, num2, '+', 'red')
dynamic_math(num1, num2, '-', 'blue')
dynamic_math(num1, num2, '*', 'green')
dynamic_math(num1, num2, '/', 'salmon')
dynamic_math(num1, num2, '//', 'magenta')
dynamic_math(num1, num2, '%', 'darkviolet')
dynamic_math(num1, num2, '|', 'gold')


# ===================
turtle.exitonclick()