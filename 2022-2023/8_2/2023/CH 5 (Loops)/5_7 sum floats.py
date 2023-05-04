a, b, h = 0.01, 1, 0.01
s = 0

while a <= 1:
  s += round(a, 2)
  a = round(a, 2) + 0.01

print(s)


a, b, h = 0.01, 1, 0.01
s = 0
N = int((b - a) / h) + 1
for i in range(N):
  s += a
  a += h

print(f"{s:.2f}")
