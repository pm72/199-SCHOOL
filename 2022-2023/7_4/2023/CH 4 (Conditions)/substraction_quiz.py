import random as r

x = r.randint(0, 9)
y = r.randint(0, 9)

print(f"x = {x}, y = {y}")

if x < y:
  x, y = y, x

answer = int(input(f"What is {x} - {y}? "))

print(f"{x} - {y} = {answer} is {x - y == answer}")

if answer != x - y:
  print(f"{x} - {y} is {x - y}")


print(f"x = {x}, y = {y}")
