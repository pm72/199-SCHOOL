from random import randint

number = randint(0, 100)

print("Guess a magic number between 0 and 100\n")

attempt = 1

guess = -1
while guess != number:
  
  guess = int(input(f"Attempt {attempt}:\nEnter your guess: "))

  if guess == number:
    print(f"YES, the number is {number}\n\n")
  elif guess > number:
    print("Your guess is too high\n\n")
  else:
    print("Your guess is too low\n\n")

  attempt += 1

input("Game over")
