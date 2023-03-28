year = int(input("Enter an year: "))

leap_year = year % 4 == 0 and year % 100 != 0 or \
            year % 400 == 0

month = int(input("Enter number of month [1..12]: "))

m = {
  'January': 31,
  'February': 28 + leap_year,
  }


if month == 1:
  m = 'January'
  days = 31
elif month == 2:
  m = 'February'
  days = 28 + leap_year
elif month == 3:
  m = 'March'
  days = 31
elif month == 4:
  m = 'April'
  days = 30
  


print(f"\n{m} {year} has {days} days")
