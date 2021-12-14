import random
n=random.randint(10**11, 10**12)
mn=10
mx=0
while (n>0):
    m = n%10
    mx = max(m, mx)
    mn = min(m, mn)
    n //= 10
print((mx+mn)**2)
