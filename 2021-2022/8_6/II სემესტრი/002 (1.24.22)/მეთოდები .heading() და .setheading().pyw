import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("წრე და რკალი")
window.setup(width=1000, height=600)

t.setheading(59)
t.write(f"კუთხე: {t.heading()}", font=('calibri', 12))
t.fd(250)




# =====================
# t.ht()
# turtle.ht()
turtle.exitonclick()