import turtle
from dynamic_math import dynamic_math


if __name__ == '__main__':
  s = turtle.getscreen()
  t = turtle.Turtle()

  t.ht()
  turtle.ht()

  turtle.title("მათემატიკური დინამიკური ოპერაციები")
  turtle.setup(width=1200, height=600)

  dynamic_math(1.56, 2.89, '/', '#fcd004')
  dynamic_math(58, 17, '+', '#acfe25')
  dynamic_math(5.28, 0, '**', '#ff3400')

  try:
    num1 = turtle.numinput("", "პირველი რიცხვი:")
    num2 = turtle.numinput("", "მეორე რიცხვი:")

    dynamic_math(num1, num2, '/', '#dd47fa')
  except TypeError:
    t.pencolor('red')
    t.write(f"Input bad Data: '{num1}' and '{num2}'", font=("georgia", 40, 'bold'), align='center')


  # ===================
  turtle.exitonclick()


