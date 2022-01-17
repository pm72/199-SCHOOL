import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("ტექსტის გამოტანა turtle ეკრანზე")
window.setup(width=1000, height=600)

t.up()
t.goto(0, 200)
t.down()

t.color('red')
t.write("მოგესალმებით ყველას!..", font=("Calibri", 40, "bold italic underline"), align='center')




# =====================
t.ht()
turtle.ht()
turtle.exitonclick()