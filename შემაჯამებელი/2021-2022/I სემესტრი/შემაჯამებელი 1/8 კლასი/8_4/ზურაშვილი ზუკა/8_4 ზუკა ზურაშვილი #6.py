import random as r
n = r.randint(10**11, 10**12)
mn = 10
mx = 0
while (n>0):
    k = a%10
    mx = max(k, mx)
    mn = min(k, mn)
    n //= 10
print((mx+mn)**2)
