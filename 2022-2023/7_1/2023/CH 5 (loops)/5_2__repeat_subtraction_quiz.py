from random import randint as r

answer = 'y'
while answer.lower() != 'n':
  number1 = r(0, 9)
  number2 = r(0, 9)

  if number1 < number2:
    number1, number2 = number2, number1

  answer = int(input(f"What is {number1} - {number2} ? "))

  while answer != number1 - number2:
    answer = int(input("Wrong answer. Try again. " +\
                       F"What is {number1} - {number2} ? "))

  print("\nYou got it!\n")

  answer = input("Continue [y / n]? ")
  print("\n")

print("Game over!")
