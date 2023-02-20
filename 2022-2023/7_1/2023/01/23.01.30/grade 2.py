score = eval(input("Enter a score: "))


# wrong code
##if score >= 60:
##  grade = 'D'
##elif score >= 70:
##  grade = 'C'
##elif score >= 80:
##  grade = 'B'
##elif score >= 90:
##  grade = 'A'
##else:
##  grade = 'F'


if score <= 60:
  grade = 'F'
elif score <= 70:
  grade = 'D'
elif score <= 80:
  grade = 'C'
elif score <= 90:
  grade = 'B'
else:
  grade = 'A'

print(f"Your grade is {grade}")
