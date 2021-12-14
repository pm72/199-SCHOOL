import random
a = random.randint(10**11, 10**12)
b = 10
c = 0
while (a>0):
    l = a%10
    c = max(l, c)
    b = min(l, b)
    a //= 10
print((b+c)**2)
