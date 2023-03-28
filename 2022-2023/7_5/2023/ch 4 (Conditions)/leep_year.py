year = int(input("Enter an year: "))

leep_year = (year % 4 == 0 and year % 100 != 0) or \
            year % 400 == 0

##if leep_year:
##  print(f"{year} is leep")
##else:
##  print(f"{year} is not leep")


print(f"{year} is leep" if leep_year else \
      f"{year} is not leep")
