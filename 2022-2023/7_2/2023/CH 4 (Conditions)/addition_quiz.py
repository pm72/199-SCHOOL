import random as r

x = r.randint(0, 9)
y = r.randint(0, 9)

answer = int(input(f"What is {x} + {y}? "))

print(f"{x} + {y} = {answer} is {x + y == answer}")

if x + y != answer:
  print(f"{x} + {y} is {x + y}")



"""
  r.randint(a, b)
  r.randrange(a, b-1)

  r.random()    range(0.0, 1.0]
  r.uniform(a, b)

  r.choice()
"""
