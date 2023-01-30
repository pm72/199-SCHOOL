import random as r

x = r.randint(0, 10)
y = r.randint(0, 10)

answer = int(input(f"What is {x} + {y}? "))

print(f"{x} + {y} = {answer} is {x + y == answer}")

if answer != x + y:
  print(f"{x} + {y} = {x + y}")



"""
  r.randint(a, b)  => int
  r.randrange(a, b-1)   => int

  r.random()   => float   [0.0 .. 1.0)
  r.uniform(a, b)  => float

  r.choice(a)
"""
