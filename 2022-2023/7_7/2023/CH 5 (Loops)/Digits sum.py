from random import randint as r

number = r(1, 10 ** 9)

print(number, "\n")

s = 0
while number:
  s += number % 10

  number //= 10


print(f"Digits sum is {s}")
