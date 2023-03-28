import random as r

lottery = r.randint(0, 99)

guess = int(input("Enter your lottery pick (two digits): "))

l_digit1 = lottery // 10
l_digit2 = lottery % 10

g_digit1 = guess // 10
g_digit2 = guess % 10

print("The lottery number is", lottery)

if guess == lottery:
  print("Exact match: you win $10,000")
elif l_digit1 == g_digit2 and \
     l_digit2 == g_digit1:
  print("Match all digits: you win $3,000")
elif l_digit1 == g_digit1 or \
     l_digit1 == g_digit2 or \
     l_digit2 == g_digit1 or \
     l_digit2 == g_digit2:
  print("Match one digit: you win $1,000")
else:
  print("Sorry, no match")

input("\nPress ENTER to exit...")
