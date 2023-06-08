import turtle as t

alpha = 0.2

def draw_rectangle(A, B, C, D, deep=10):
  if deep < 1:
    return

  for M, N in (A, B), (B, C), (C, D), (D, A):
    t.up()
    t.goto(M)
    t.down()
    t.goto(N)


  t.done()


    

# =================
draw_rectangle((-100, -100), (500, -100), (500, 500), (-100, 500))
