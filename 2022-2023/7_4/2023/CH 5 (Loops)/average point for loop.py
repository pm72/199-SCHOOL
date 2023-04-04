N = 20
s = 0

print("POINTS:")

for i in range(N):
  data = eval(input())

  s += data

  print(data)

print(f"The average is {(s / N):.2f}")
