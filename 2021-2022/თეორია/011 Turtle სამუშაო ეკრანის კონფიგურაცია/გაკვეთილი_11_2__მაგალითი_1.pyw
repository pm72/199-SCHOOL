import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Hello turtle!")
turtle.bgcolor('DarkOrchid')

t.pencolor('Salmon')
t.fillcolor('Chartreuse')
t.pensize(5)
t.speed(7)

##t.goto(0, 100)
##t.goto(100, 100)
##t.goto(100, 0)
##t.home()

t.begin_fill() 
t.goto(0, 100)
t.goto(100, 100)
t.goto(100, 0)
t.home()
t.end_fill()

 



# =================
t.hideturtle()
turtle.hideturtle() 
turtle.done()
