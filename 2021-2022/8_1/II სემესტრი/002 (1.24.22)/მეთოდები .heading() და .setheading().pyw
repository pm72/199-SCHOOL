import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("წრე და რკალი")
window.setup(1000, 600)

t.write(f"კუთხე: {t.heading()}", font=('calibri', 12))
t.fd(200)

t.setheading(60)
t.write(f"კუთხე: {t.heading()}", font=('calibri', 12))
t.fd(200)




# ===================
# t.ht()
# turtle.ht()
turtle.exitonclick()