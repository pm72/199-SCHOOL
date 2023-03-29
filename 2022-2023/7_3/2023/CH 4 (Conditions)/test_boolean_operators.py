x = int(input("Enter an integer: "))

if x % 3 == 0 and x % 2 == 0:
  print(f"{x} divisibla by 2 and 3")

if x % 3 == 0 or x % 2 == 0:
  print(f"{x} divisibla by 2 or 3")

if (x % 3 == 0 or x % 2 == 0) and \
   not (x % 3 == 0 and x % 2 == 0):
  print(f"{x} divisibla by 2 or 3, but not both")
