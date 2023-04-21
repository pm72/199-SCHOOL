a, b, h = 2.34, 3.68, 0.014
s = 0
              # a = 2.34   2.34+0.014
while a <= b: # s = 0      2.34 + (2.34+0.014)
  s += a      #     2.34
  a += h

print(s)


a, b, h = 2.34, 3.68, 0.014
s = 0

for i in range(a, b+h, h):
  s += i

print(s)
