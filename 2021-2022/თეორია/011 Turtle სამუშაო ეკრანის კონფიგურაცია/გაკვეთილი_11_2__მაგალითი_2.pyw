import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Hello turtle!")
turtle.bgcolor('DarkOrchid')

##t.color('Salmon', 'Chartreuse')
t.pen(pencolor='Salmon', fillcolor='Chartreuse',
      pensize=5, speed=7)

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
