from random import randint as r

number = r(1, 100)

print("Guess a magic number between 0 and 100\n")

guess = 0
attempt = 1
while guess != number:
  print(f"Attempt #{attempt}:")
  guess = int(input("Enter your guess: "))
  
  if guess == number:
    print(f"Yes, the number is {number}\n")
  elif guess > number:
    print("Your guess is too high\n")
  else:
    print("Your guess is too low\n")

  attempt += 1


input("\n\nGame over...\n")
