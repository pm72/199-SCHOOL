from random import randint as r
from time import time as t

count = 1
correct_answer = 0
start_time = t()
amount_count = r(5, 10)

print(f"You have {amount_count} attempts\n")

while count <= amount_count:
  x = r(0, 9)
  y = r(0, 9)

  if x < y:
    x, y = y, x
  
  answer = int(input(f"What is {x} - {y}? "))

  if answer == x - y:
    print("You are correct!\n")
    correct_answer += 1
  else:
    print("Your answer is wrong.\n" + \
          f"{x} - {y} = {x - y}\n")

  count += 1

end_time = t()

print(f"Correct count is {correct_answer} of " + \
      f"{amount_count}\n" + \
      f"Test time is {end_time - start_time:.2f} seconds")
      
