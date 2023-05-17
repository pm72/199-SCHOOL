# break

number = 0
s = 0

while True:
  number += 1
  s += number

  if s >= 100:
    break

print(number)
print(s)
