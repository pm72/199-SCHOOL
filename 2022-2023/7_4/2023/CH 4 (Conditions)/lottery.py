from random import randint as r
import sys
balance = 0

while balance < 100:
  balance = eval(input("Fill your balance: "))

while balance >= 100:
  lottery = r(10, 99)
  guess = int(input("Enter your lottery pick (two digits): "))

  if guess == 0:
    print(f"Balance: ${balance}")
    print(f"Game is over")

    input()
    sys.exit()

  lottery_digit1 = lottery // 10
  lottery_digit2 = lottery % 10

  guess_digit1 = guess // 10
  guess_digit2 = guess % 10

  balance -= 100

  if lottery == guess:
    print("Exact match: you win $10,000!!!")
    balance += 10000
  elif lottery_digit1 == guess_digit2 and \
       lottery_digit2 == guess_digit1:
    print("Match all digits: you win $3,000")
    balance += 3000
  elif lottery_digit1 == guess_digit1 or \
       lottery_digit1 == guess_digit2 or \
       lottery_digit2 == guess_digit1 or \
       lottery_digit2 == guess_digit2:
    print("Match one digit: you win $1,000")
    balance += 1000
  else:
    print("Sorry, no match")


  print(f"\nLottery number is {lottery}")
  print(f"\nYour balance: {balance}\n")
  
print(f"Game is over")
