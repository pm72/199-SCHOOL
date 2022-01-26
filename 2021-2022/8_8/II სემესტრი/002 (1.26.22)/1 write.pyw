import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("ტექსტის დაწერა tutle ეკრანზე")
window.setup(1000, 600)

t.pen(pencolor='brown')

# t.write("Hello, there!..", font=('calibri', 40, 'bold italic underline'))
t.up()
t.goto(0, 200)
t.down()
t.write("გილოცავთ შობას და ახალ წელს!", font=('calibri', 40, 'bold italic underline'),
        align='center')




# =========================
turtle.exitonclick()