year = int(input("Enter an year: "))

leap_year = year % 4 == 0 and year % 100 != 0 or \
            year % 400 == 0

if leap_year:
  print(f"{year} is leap year")
else:
  print(f"{year} is not leap year")
  
