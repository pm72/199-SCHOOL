import random as r
import sys

balance = 0
while balance < 100:
  balance = eval(input("Fill your balance [min $100]: "))

while balance >= 100:
  lottery = r.randint(0, 99)

  guess = 0
  while guess < 10 or guess > 99:
    guess = int(input("Enter your lottery pick (two digits)" + \
                      "(0 - Exit): "))

    if guess == 0:
      print(f"\nBalance: {balance}\n\n")
      input("Game over...")
      sys.exit()

  lottery_digit1 = lottery // 10
  lottery_digit2 = lottery % 10

  guess_digit1 = guess // 10
  guess_digit2 = guess % 10

  balance -= 100

  if guess == lottery:
    print("Exact match: you win $10000\n")
    balance += 10000
  elif guess_digit1 == lottery_digit2 and \
       guess_digit2 == lottery_digit1:
    print("Match all digits: you win $3000\n")
    balance += 3000
  elif guess_digit1 == lottery_digit1 or \
       guess_digit1 == lottery_digit2 or \
       guess_digit2 == lottery_digit1 or \
       guess_digit2 == lottery_digit2:
    print("Match one digit: you win $500")
    balance += 500
  else:
    print("Sorry, no match")

  print(f"\nLottery number was {lottery}")

  print(f"\nBalance: {balance}\n\n")


input("Game over...")
