from template.main_window import *

s = turtle.getscreen()
t = turtle.Turtle()

t.pen(pencolor='red', fillcolor='yellow', pensize=2)

w = 100
h = 150

##t.left(60)
##t.forward(w)
##
##t.left(60)
##t.forward(w)
##
##t.left(60)
##t.forward(w)
##
##t.left(60)
##t.forward(w)
##
##t.left(60)
##t.forward(w)
##
##
##t.home()

t.begin_fill()
for i in range(6):
  t.forward(w)
  t.left(60)
t.end_fill()



# ===========
turtle.done()
