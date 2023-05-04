a = 0.01
s = 0

while a <= 1:
  s += round(a, 2)
  a = round(a, 2) + 0.01

print(s)


a = 0.01
s = 0
N = int((1 - 0.01) / 0.01) + 1
for i in range(N):
  s += a
  a += 0.01

print(f"{s:.2f}")
