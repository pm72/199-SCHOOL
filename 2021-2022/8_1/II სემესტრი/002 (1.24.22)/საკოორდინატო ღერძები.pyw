import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("საკოორდინატო ღერძები")
window.setup(1000, 600)

t.pen(pensize=3, pencolor='brown')

# 0 გრადუსი
t.fd(200)
t.write(t.heading(), font=(12))

t.up()
t.home()
t.down()

# 90 გრადუსი
t.setheading(90)
t.fd(200)
t.write(t.heading(), font=(12))

t.up()
t.home()
t.down()

# 180 გრადუსი
t.setheading(180)
t.fd(200)
t.write(t.heading(), font=(12))

t.up()
t.home()
t.down()

# 270 გრადუსი
t.setheading(270)
t.fd(200)
t.write(t.heading(), font=(12))

t.up()
t.home()
t.down()




# ===================
# t.ht()
# turtle.ht()
turtle.exitonclick()