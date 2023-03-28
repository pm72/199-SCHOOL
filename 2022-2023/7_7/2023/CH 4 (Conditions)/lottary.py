from random import randint
import sys

balance = 0
while balance < 100:
  balance = eval(input("Fill your balance [min $100]: "))

while balance >= 100:
  lottary = randint(10, 99)

  guess = 0
  while guess < 10 or guess > 99:
    guess = int(input("Enter two digit number " + \
                      "(0 - Exit): "))

    if guess == 0:
      print(f"\nBalance: ${balance}")
      input("\n\nGame over...")
      sys.exit()

  lottary_digit1 = lottary // 10
  lottary_digit2 = lottary % 10

  guess_digit1 = guess // 10
  guess_digit2 = guess % 10

  balance -= 100

  if guess == lottary:
    print("Exact match! You win $10000")
    balance += 10000
  elif lottary_digit1 == guess_digit2 and \
       lottary_digit2 == guess_digit1:
    print("All digits match. You win $3000")
    balance += 3000
  elif lottary_digit1 == guess_digit1 or \
       lottary_digit1 == guess_digit2 or \
       lottary_digit2 == guess_digit1 or \
       lottary_digit2 == guess_digit2:
    print("One digit match. You win $500")
    balance += 500
  else:
    print("Sorry, no digits match...")
    print(f"\nLottary number was {lottary}")

  print(f"\nBalance: ${balance}\n\n")


input("Game over...")
