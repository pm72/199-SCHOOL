##s = 0
##i = 1
##N = 25

##print("POINTS:")

##while i <= N:
##  data = eval(input())
##
##  s += data
##
##  i += 1
##
##  print(data)
##
##print(f"\n\nAverage point: {(s / N):.2f}")

s = 0
N = 5

for i in range(1, N + 1):
  data = eval(input())

  s += data

print(f"\n\nAverage point: {(s / N):.2f}")
