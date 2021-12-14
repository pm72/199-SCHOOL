import random as r
a = r.randint(10 ** 11 , 10 ** 12)
print(a)
b = 10
c = 0
while (a > 0):
    d = a % 10
    b = min (d , b)
    c = max (d , c)
    a //= 10

print((c + b) ** 2)

