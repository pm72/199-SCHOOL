a, b, h = 2.31, 3.58, 0.014
s = 0

while a <= b:
  s += a
  a += h

print(s)


a, b, h = 2.31, 3.58, 0.014
s = 0
N = int((b - a) / h) + 1

for i in range(N):
  s += a
  a += h

print(s)