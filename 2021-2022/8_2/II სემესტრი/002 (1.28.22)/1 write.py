import turtle

window = turtle.getscreen()
t = turtle.Turtle()

t.ht()
turtle.ht()

turtle.title("წარწერა turtle ეკრანზე")
turtle.setup(1200, 600)

t.pen(pencolor='magenta')

# t.write("Hello, there!..", font=('calibri', 40, 'italic underline bold'))

t.up()
t.goto(0, 200)
t.down()

t.write("მოგესალმებით ყველას! დღეს 28 იანვარია...",
        font=('calibri', 40, 'italic underline bold'),
        align='center')

# ================
turtle.exitonclick()