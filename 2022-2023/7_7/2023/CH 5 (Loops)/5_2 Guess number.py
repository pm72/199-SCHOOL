from random import randint as r

number = r(0, 100)

print("Guess a magic number between 0 and 100\n")

guess = -1
while guess != number:
  guess = int(input("Enter a number: "))

  if guess == number:
    print(f"Yes, the number is {number}\n")
  elif guess > number:
    print("Your guess is too high\n")
  else:
    print("Your guess is too low\n")


input("\nGame over...")
