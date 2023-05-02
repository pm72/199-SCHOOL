x = 0.01
s = 0

##while x <= 1:
##  print(x)
##  s += x
##  x += 0.01

while x <= 1:
  s += round(x, 2)
  x = round(x, 2) + 0.01

print(s)


x = 0.01
s = 0
N = int((1 - 0.01) / 0.01) + 1
for i in range(N):
  s += x
  x += 0.01

print(f"{s:.2f}")
