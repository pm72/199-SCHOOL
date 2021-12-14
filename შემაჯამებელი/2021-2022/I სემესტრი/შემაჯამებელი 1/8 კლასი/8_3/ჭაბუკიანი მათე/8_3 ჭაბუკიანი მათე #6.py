import random
x = random.randint(10**11, 10**12)
mn = 10
mx = 0
while (x>0):
    y = x%10
    mx = max(y, mx)
    mn = min(y, mn)
    x//= 10
print((mx + mn)**2)
