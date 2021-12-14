import random
x = random.randint(10**11,10**12)
fl = 10
fm = 0
while (x>0):
    n = x%10
    fl = min(n, fl)
    fm = max(n, fm)
    x //= 10
print((fm + fl)**2)
