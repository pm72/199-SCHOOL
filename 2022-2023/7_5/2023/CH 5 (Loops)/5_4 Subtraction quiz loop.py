from random import randint as r
from time import time as t

correct = 0
count = 1
NUMBER_OF_QUESTION = 5

start = t()

while count <= NUMBER_OF_QUESTION:
  x = r(0, 9)
  y = r(0, 9)

  if x < y: x, y = y, x

  answer = int(input(f"What is {x} - {y}? "))

  if answer == x - y:
    print("You are correct!\n")
    correct += 1
  else:
    print("Your answer is wrong.\n" +\
          f"{x} - {y} = {x - y}\n")

  count += 1

test_time = t() - start

print(f"Correct count is {correct} out of {NUMBER_OF_QUESTION}")
print(f"Test time is {test_time:.2f} seconds")


# ================
input("\n\nDone!..\n")
