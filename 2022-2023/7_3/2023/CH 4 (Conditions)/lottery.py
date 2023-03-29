from random import randint
import sys

balance = 0
while balance < 100:
  balance = eval(input("Fill your balance [min $100]: "))

while balance >= 100:
  lottery = randint(10, 99)

  guess = 0
  while guess < 10 or guess > 99:
    guess = int(input("Enter your lottery pick (two digits)\n" + \
                      "[0 - Exit]: "))

    if guess == 0:
      print(f"\nYour balance is ${balance}")
      input("\n\nGame over!..")
      sys.exit()

  balance -= 100
  
  lottery_digit1 = lottery // 10
  lottery_digit2 = lottery % 10

  guess_digit1 = guess // 10
  guess_digit2 = guess % 10

  if guess == lottery:
    print("Exact match: you win $10,000")
    balance += 10000
  elif guess_digit1 == lottery_digit2 and \
       guess_digit2 == lottery_digit1:
    print("Match all digits: you win $3,000")
    balance += 3000
  elif guess_digit1 == lottery_digit1 or \
       guess_digit2 == lottery_digit1 or \
       guess_digit1 == lottery_digit2 or \
       guess_digit2 == lottery_digit2:
    print("Match one digit: you win $1,000")
    balance += 1000
  else:
    print("Sorry, no match")

  print(f"\nYour balance is ${balance}")
  print(f"\nlottery: {lottery}\n\n")



input("\n\nGame over!..")
