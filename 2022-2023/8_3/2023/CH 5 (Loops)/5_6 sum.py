a, b, h = 0.15, 0.36, 0.015
s = 0
arr = []

while a <= b:
  arr.append(a)
  s = round(s + a, 3)
  a = round(a + h, 3)

print(arr)
print(s)

print()

'''
range(a, b-1, h)

'''

a, b, h = 0.15, 0.36, 0.015
s = 0
N = int((b - a) / h) + 1
arr = []

for i in range(N):
  arr.append(a)
  s = round(s + a, 3)
  a = round(a + h, 3)

print(arr)
print(s)
