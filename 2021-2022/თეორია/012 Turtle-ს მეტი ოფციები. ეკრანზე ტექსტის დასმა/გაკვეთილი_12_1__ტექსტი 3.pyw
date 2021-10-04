import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Python turtle - text")

t.pen(speed=4)

t.penup()
t.goto(-200, 200)
t.pendown()

t.write("Hello there!", move=True, font=('Calibri', 40, 'normal'))

# georgian text
t.penup()
t.goto(-300, 100)
t.pendown()

t.pencolor('red')
##t.write("მოგესალმებით ყველას!", move=True,
##        font=('calibri', 40, 'bold'))
t.write("Hello there!", move=True,
        font=('georgia', 40, 'bold', 'italic', 'underline'))



# =================
turtle.done()
