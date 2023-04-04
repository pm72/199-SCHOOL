s = 0
N = 20
i = 1

print("POINTS:")

while i <= N:
  data = eval(input())
  s += data

  i += 1
  
  print(data)

print(f"\nThe average: {(s / N):.2f}")
