# 5.15.1

number = 0
s = 0

while s <= 100:
  number += 1
  s += number

print(number)
print(s, "\n\n")



# ===============
# 5.15.2

number = 0
s = 0

while number < 20 and (number != 10 or number != 11):
  number += 1
  s += number


print(s)
print("\n\nDone!..\n")
