from random import randint

answer = 'y'

while answer.lower() != 'n':
  number1 = randint(0, 9)
  number2 = randint(0, 9)

  if number1 < number2:
    number1, number2 = number2, number1

  answer = int(input(f"What is {number1} - {number2} ? "))

  while number1 - number2 != answer:
    answer = int(input("Wrong answer. Try again. " + \
                       f"What is {number1} - {number2} ? "))

  print("You got it!")

  answer = input("\n\nContinue [y / n]? ")
  print("\n")

input("Game over")
