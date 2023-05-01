a = 0.01
s = 0

##while a <= 1:
##  s += a
##  a += 0.01

##while a <= 1:
##  s += round(a, 2)
##  a = round(a, 2) + 0.01
##
##print(s)
##
##
##a = 0.01
##s = 0
##N = int((1 - 0.01) / 0.01) + 1
##
##for i in range(N):
##  s += a
##  a += 0.01
##
##print(f"{s:.2f}")


a, b, h = 0.256, 0.369, 0.0013
N = int((b - a) / h) + 1
for i in range(N):
  print(a)
  s += a
  a += h

print(s)
