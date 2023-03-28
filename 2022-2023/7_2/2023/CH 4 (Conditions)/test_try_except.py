import sys

"""
  try:
  except:
"""

##x = 0.0
b = True
while b:
  try:
    x = int(input("Enter an integer: "))
    b = False
  except ValueError:
    print("\nPlease, enter an integer...\n")
  except NameError:
    ...
##    sys.exit()

print(x)
