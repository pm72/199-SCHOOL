import random
n = random.randint(10**11, 10**12)
xy = 10
xz = 0
while (n>0):
    a = n%10
    xz = max(a, xz)
    xy = min(a, xy)
    n //= 10
print((xy+xz)**2)
