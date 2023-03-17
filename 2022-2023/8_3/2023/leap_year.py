year = int(input("Enter year: "))  # 1900

leap_year = year % 4 == 0 and year % 100 != 0 or \
            year % 400 == 0

if leap_year:
  print(f"{year} is leap year")
else:
  print(f"{year} isn't leap year")


print(f"{year} is leap year" if leap_year else f"{year} isn't leap year")
