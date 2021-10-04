import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Python turtle - text")

t.penup()
t.goto(200, 200)
t.pendown()
##t.write("Hello there!")
t.write("Hello there!", move=True)




# =================
t.hideturtle()
turtle.done()
