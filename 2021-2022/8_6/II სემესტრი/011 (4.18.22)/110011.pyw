import turtle

ypos = 200


def dynamic_math(x, y, op, col):
  global ypos
  t.pencolor(col)
  t.pu()
  t.goto(0, ypos)
  t.pd()

  display = f"{num1} + {num2} = {num1 + num2}"

  t.write(display, font=("georgia", 45, 'bold'), align='center')

  ypos -= 80


# =====> RUN PROGRAM <=====
s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Colorful and dynamic Math")
turtle.setup(width=1000, height=600)
turtle.bgcolor('lightyellow')

num1 = int(turtle.numinput("Input numbers", "First Number:"))
num2 = int(turtle.numinput("Input numbers", "Second Number:"))

dynamic_math(num1, num2, '+', 'red')
dynamic_math(num1, num2, '-', 'blue')
dynamic_math(num1, num2, '*', 'green')
dynamic_math(num1, num2, '/', 'salmon')
dynamic_math(num1, num2, '//', 'magenta')
dynamic_math(num1, num2, '%', 'darkviolet')



# ================
t.ht()
turtle.ht()
turtle.exitonclick()