import random
t = random.randint(10**11, 10**12)
mn = 10
mx = 0
while (t>0):
    k = t%10
    mx = max(k, mx)
    mn = min(k, mn)
    t //= 10
print((mx+mn)**2)
