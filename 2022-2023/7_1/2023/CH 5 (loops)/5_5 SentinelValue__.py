data = -1
s = 0
students = 0
while data != 0:
  students += 1
  data = eval(input())

  s += data

print(f"The sum is {s}")
print(f"Total students: {students - 1}")
