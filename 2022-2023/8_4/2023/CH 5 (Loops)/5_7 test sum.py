##i = 0.01
##s = 0
##
##while i <= 1.0:
##  s += round(i, 2)
##  i = round(i, 2) + 0.01
##
##print(s)
##
##
##i = 0.01
##N = int((1 - 0.01) / 0.01) + 1
##s = 0
##
##for x in range(N):
##  s += i
##  i += 0.01
##
##print(s)



a, b, h = 0.256, 0.369, 0.0013
s = 0
N = int((b - a) / h) + 1
for i in range(N):
  print(a)
  s += a
  a += h

print(s)
