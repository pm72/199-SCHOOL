from random import randint

lottary = randint(10, 99)

guess = 0
while guess < 10 or guess > 99:
  guess = int(input("Enter two digit number: "))

lottary_digit1 = lottary // 10
lottary_digit2 = lottary % 10

guess_digit1 = guess // 10
guess_digit2 = guess % 10

if guess == lottary:
  print("Exact match! You win $10000")
elif lottary_digit1 == guess_digit2 and \
     lottary_digit2 == guess_digit1:
  print("All digits match. You win $3000")
elif lottary_digit1 == guess_digit1 or \
     lottary_digit1 == guess_digit2 or \
     lottary_digit2 == guess_digit1 or \
     lottary_digit2 == guess_digit2:
  print("One digit match. You win $500")
else:
  print("Sorry, no digits match...")

print(f"\nLottary number was {lottary}")
