import random
x = random.randint(10**11, 10**12)
mn = 10
mx = 0
while (x>0):
    l = x%10
    mx = max(l, mx)
    mn = min(l, mn)
    x //= 10
print((mx+mn)**2)