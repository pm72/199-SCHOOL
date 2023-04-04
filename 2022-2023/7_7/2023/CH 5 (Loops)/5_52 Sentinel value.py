s = 0
N = 20

print("POINTS:")

for i in range(N):    # 0, 1, 2, ..., 19
  data = eval(input())
  s += data
  
  print(data)

print(f"\nThe average: {(s / N):.2f}")
