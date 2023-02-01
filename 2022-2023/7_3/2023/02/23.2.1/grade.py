##score = int(input("Enter score [max = 100, min = 0]: "))   # DRY

score = -1

if score < 0 or score > 100:
  score = int(input("Enter score [max = 100, min = 0]: "))

##if score > 90:
##  grade = 10
##else:
##  if score > 80:
##    grade = 9
##  else:
##    if score > 70:
##      grade = 8
##    else:
##      if score > 60:
##        grade = 7
##      else:
##        if score > 50:
##          grade = 6
##        else:
##          grade = 5


if score > 90:
  grade = 10
elif score > 80:
  grade = 9
elif score > 70:
  grade = 8
elif score > 60:
  grade = 7
elif score > 50:
  grade = 6
else:
  grade = 5


print(f"\nResult:\n" + \
      f"Score: {score}\n" + \
      f"Grade: {grade}")
        
