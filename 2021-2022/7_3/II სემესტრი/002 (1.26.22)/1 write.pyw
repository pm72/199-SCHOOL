import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("წარწერები turtle ეკრანზე")
window.setup(1000, 600)

t.pen(pencolor='red')
t.up()
t.goto(0, 200)
t.down()
# t.write("Hello, there!..", font=("calibri", 40, 'bold italic underline'), align='center')
t.write("გილოცავთ შობას და ახალ წელს!", font=("calibri", 40, 'bold italic underline'), align='center')




# =======================
t.ht()
turtle.ht()
turtle.exitonclick()