import random as r

lottery = r.randint(0, 99)

guess = int(input("Enter your lottery pick (two digits): "))

lottery_digit1 = lottery // 10
lottery_digit2 = lottery % 10

guess_digit1 = guess // 10
guess_digit2 = guess % 10

print("The lottery number is", lottery)

if guess == lottery:
  print("Exact match: you win $10,000\n")
elif guess_digit1 == lottery_digit2 and \
     guess_digit2 == lottery_digit1:
  print("Match all digits: you win $3,000\n")
elif guess_digit1 == lottery_digit1 or \
     guess_digit1 == lottery_digit2 or \
     guess_digit2 == lottery_digit1 or \
     guess_digit2 == lottery_digit2:
  print("Match one digit: you win $1,000")
else:
  print("Sorry, no match")