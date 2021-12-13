import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# ეკრანის კონფიგურაცია
s.setup(1000, 600)
s.bgcolor('black')
s.title('მართკუდხედი და წრე სხვადასხვა მხარეს')

t.speed(0)
# t._tracer(0)

colors = ['red', 'green', 'yellow',
'magenta', 'blue', 'cyan']

r = 100
n = 3

for i in range(1):
    for color in colors:
        t.pencolor(color)
        t.circle(r, 360 / len(colors))

    t.lt(10)






# ===============
turtle.exitonclick()
