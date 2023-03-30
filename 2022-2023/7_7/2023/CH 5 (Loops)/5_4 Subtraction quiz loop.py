from random import randint as r
from time import time as t

NUMBER_OF_QUESTION = 5
correct_count = 0
count = 0

start = t()

while count < NUMBER_OF_QUESTION:
  x = r(0, 9)
  y = r(0, 9)

  if x < y: x, y = y, x

  answer = int(input(f"What is {x} - {y}? "))

  if answer == x - y:
    print("You are correct!")
    correct_count += 1
  else:
    print("Your answer is wrong.\n" + \
          f"{x} - {y} is {x - y}")

  count += 1

  print("\n")


test_time = t() - start

print(f"Current count is {correct_count} of {NUMBER_OF_QUESTION}")
print(f"Test time is {test_time:.2f} seconds")


