from random import randint as r

number = r(0, 10 ** 6)

print("Guess a magic number between 0 and 100")

guess = -1
n = 1
while guess != number:
  print(f"{n}:")
  guess = eval(input("Enter your guess: "))

  if guess == number:
    print("Yes, the number is\n", number)
  elif guess > number:
    print("Your guess is too high\n")
  else:
    print("Your guess is too low\n")

  n += 1
