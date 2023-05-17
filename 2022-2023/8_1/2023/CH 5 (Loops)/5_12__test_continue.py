# continue

number = 0
s = 0

while number < 20:
  number += 1

  if number == 10 or number == 11:
    continue

  s += number

print(number)
print(s)
