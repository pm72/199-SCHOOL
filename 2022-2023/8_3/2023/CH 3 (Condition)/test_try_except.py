import sys

"""
  try:
    ...
  except:
    ...
"""

##while True:
##  try:
##    x = int(input("Enter an integer: "))
##    break
##  except:
##    print("\nPlease, enter an integer...\n")
##    sys.exit()

##b = True
##while b:
##  try:
##    x = int(input("Enter an integer: "))
##    b = False
##  except:
##    print("\nPlease, enter an integer...\n")

x = 0.0
while type(x) == float:
  try:
    x = int(input("Enter an integer: "))
  except:
    print("\nPlease, enter an integer...\n")

print(x)
