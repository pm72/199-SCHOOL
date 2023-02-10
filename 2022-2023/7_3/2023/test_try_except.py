import sys

while True:
  try:
    x = int(input("Enter an integer: "))
    break
  except ValueError:
    print("\nPlease, enter an integer...\n")
##    sys.exit()

print(x)
