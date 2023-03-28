from random import randint as r

answer = 'y'
while answer.lower() != 'n':
  x = r(0, 9)
  y = r(0, 9)

  if x < y:
    x, y = y, x

  answer = int(input(f"What is {x} - {y} ? "))

  while answer != x - y:
    answer = int(input("Wrong answer. Try again. " + \
                       f"What is {x} - {y}? "))

  print("You got it!")

  answer = input("\n\nContinue [y / n]? ")

  print("\n")


input("Quiz is complete...")
