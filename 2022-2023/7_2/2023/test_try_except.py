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
  except:
    print("\nPlease, enter an integer...\n")
##    sys.exit()

print(x)
