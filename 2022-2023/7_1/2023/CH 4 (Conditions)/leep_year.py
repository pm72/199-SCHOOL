##year = int(input("Enter a year: "))
##leap_year = (year % 4 == 0 and year % 100 != 0) or \
##            year % 400 == 0

##if leap_year:
##  print(f"{year} is leap.")
##else:
##  print(f"{year} is not leap.")


# ტერნარული ოპერატორი
##print(f"{year} is leap" if leap_year else \
##      f"{year} is not leap.")


x = 56
if x > 0:
  y = 1
else:
  y = -1

print(y)
print(1 if x > 0 else -1)
