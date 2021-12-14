import random
y = random.randint(10**11, 10**12)
mn = 10
mx = 0
while (y>0):
    x = y%10
    mx = max(x, mx)
    mn = min(x, mn)
    y//= 10
print((mx + mn)**2)
