import turtle
from dynamic_math import dynamic_math


if __name__ == '__main__':
  s = turtle.getscreen()
  t = turtle.Turtle()

  turtle.title("დინამიური მათემატიკური ოპერაციები")
  turtle.setup(width=1000, height=600)
  turtle.bgcolor('lightyellow')

  num1 = 45
  num2 = 23

  dynamic_math(num1, num2, '/', '#f400d7')
  dynamic_math(1.58, 5.96, '*', '#d40157')
  dynamic_math(1.58, 5.96, '**', '#f00')
  dynamic_math(1.58, 0, '/', '#f00')

  t.ht()
  turtle.ht()


  # =================
  turtle.exitonclick()