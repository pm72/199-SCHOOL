a, b, h = 0.01, 1, 0.01
s = 0
N = 0

while a <= b:
  s += round(a, 2)
  a = round(a, 2) + h

print(s)


# ===============
a, b, h = 0.01, 1, 0.01
s = 0
N = int((b - a) / h) + 1

for i in range(N):
  s += a
  a += h

print(f"{s:.2f}")
