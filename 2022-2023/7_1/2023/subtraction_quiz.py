import random as r

x = r.randint(1, 9)
y = r.randint(1, 9)

if y > x:
  x, y = y, x

answer = int(input(f"What is {x} - {y}? "))

if x - y == answer:
  print("You are correct!")
else:
  print(f"Your answer is wrong!\n" + \
        f"{x} - {y} is {x - y}")
