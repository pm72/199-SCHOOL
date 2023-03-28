from random import randint as r

number = r(0, 10**6)

print("Guess a magic number between 0 and 100\n")

attempt = 1
guess = -1
while guess != number:
  guess = int(input(f"Attempt #{attempt}:\n" +\
                    "Enter your guess: "))

  if guess == number:
    print(f"Yes, the number is {number}\n")
  elif guess > number:
    print("Your guess is too high\n")
  else:
    print("Your guess is too low\n")

  attempt += 1

print("Game over...")
