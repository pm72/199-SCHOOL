import sys

s = 0
i = 1
N = 20

while i <= N:
##  data = eval(input(f"{i}: Enter a point: "))
  data = eval(input())
  
  s += data

  i += 1

print(f"The average is {(s / N):.2f}")
