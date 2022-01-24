import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("წრეწირი და რკალი")
window.setup(width=1000, height=600)

t.setheading(60)
t.write(f"კუთხე: {t.heading()}", font=('calibri', 12))
t.fd(200)




# ===============================
# t.ht()
# turtle.ht()
turtle.exitonclick()