N = 20
s = 0
i = 1

print("POINTS:")

while i <= N:
  data = eval(input())

  s += data
  i += 1

  print(data)

print(f"The average is {(s / N):.2f}")
