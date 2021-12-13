import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# ეკრანის კონფიგურაცია
s.setup(1000, 600)
s.title('მართკუთხედი და წრეწირი სხვადასხვა მხარეს')
s.bgcolor('DarkOrchid')

t.speed(0)

t.up()
t.goto(200, 150)

t.down()

t.pencolor('Violet')
t.write("გამარჯობა თქვენ!", font=('calibri', 45, 'bold italic underline'),
align='center')




# ==============
turtle.ht()
t.ht()

turtle.exitonclick()
