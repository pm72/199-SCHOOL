# Mini project - draw mandala (with just straight lines )

import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# Create the square base first
t.goto(0, 100)
t.goto(100, 100)
t.goto(100, 0)
t.home()

# First tilted square
t.goto(50, 50)
t.goto(0, 100)
t.goto(-50, 50)
t.home()

# Second tilted square
t.goto(50, -50)
t.goto(100, 0)
t.goto(0, 100)

# 3rd tilted square
t.goto(50, 150)
t.goto(100, 100)
t.goto(50, 50)

# 4th tilted square
t.goto(100, 100)
t.goto(150, 50)
t.goto(100, 0)




# =================
t.hideturtle()
turtle.hideturtle()
turtle.done()
