import random as r

x = r.randint(0, 10)
y = r.randint(0, 10)

answer = int(input(f"What is {x} + {y}? "))

print(f"{x} + {y} = {answer} is {x + y == answer}")


if x + y != answer:
  print(f"{x} + {y} = {x + y}")
