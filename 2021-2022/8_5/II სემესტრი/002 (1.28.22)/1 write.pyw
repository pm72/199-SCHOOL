import turtle

window = turtle.getscreen()
t = turtle.Turtle()

turtle.title("ტქსტი turtle ეკრანზე")
turtle.setup(1000, 600)

t.pen(pencolor='violet')

# t.write("Hello, there!..", font=('calibri', 40, 'italic underline bold'))
t.write("მოგესალმებით ყველას! დღეს 28 იანვარია...", font=('calibri', 40, 'italic underline bold'))

# ====================
turtle.exitonclick()