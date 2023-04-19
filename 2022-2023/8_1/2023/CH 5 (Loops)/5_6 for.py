'''
a = 0.56  b = 3.69, h = 0.031
[0.56, 3.69, 0.031]

'''

a, b, h = 0.56, 3.69, 0.031
s = 0
while a <= b:
  s += a
  a += h

print(s)

a, b, h = 0.56, 3.69, 0.031
s = 0
for i in range(a, b+1, h):
  s += a

print(s)
