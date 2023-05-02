x = 0.01
s = 0
##while x <= 1:
##  s += x
##
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


a, b, h = 0.0258, 0.0369, 0.00011
N = int((b - a) / h) + 1
s = 0
for i in range(N):
  s += a
  a += h

print(s)
