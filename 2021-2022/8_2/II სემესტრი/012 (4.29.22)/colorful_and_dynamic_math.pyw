import turtle
from helper import dynamic_math


# =====> RUN MAIN PROGRAM <=====
s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Colorful and dynamic Math")
turtle.setup(width=1000, height=600)
turtle.bgcolor("lightyellow")

t.ht()
turtle.ht()

num1 = turtle.numinput("Input numbers", "First number:")
num2 = turtle.numinput("Input numbers", "Second number:")

try:
  dynamic_math(int(num1), int(num2), '+', 'red')
  dynamic_math(int(num1), int(num2), '-', 'blue')
  dynamic_math(int(num1), int(num2), '*', 'green')
  dynamic_math(int(num1), int(num2), '/', 'salmon')
  dynamic_math(int(num1), int(num2), '//', 'magenta')
  dynamic_math(int(num1), int(num2), '%', 'darkviolet')
  dynamic_math(int(num1), int(num2), '|', 'gold')
except TypeError:
  t.pencolor('red')
  display = f"Input bad values for {num1} and {num2}"
  t.write(display, align='center', font=("georgia", 35, 'bold'))


# ====================
turtle.exitonclick()