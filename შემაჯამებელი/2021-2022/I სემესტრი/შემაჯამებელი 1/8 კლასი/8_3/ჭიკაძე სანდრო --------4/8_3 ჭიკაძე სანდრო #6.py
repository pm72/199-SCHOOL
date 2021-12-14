import random
a = random.randint(10**11, 10**12)
n = 10
x =0
while (a>0):
    b = a%10
    x = max(b, x)
    n = min(b, n)
    a//= 10
print((x+n)**2)
