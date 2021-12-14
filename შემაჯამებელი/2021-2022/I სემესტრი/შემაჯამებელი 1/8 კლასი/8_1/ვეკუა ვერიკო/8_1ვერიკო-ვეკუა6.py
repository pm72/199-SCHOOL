import random

p = random.randint(10**11, 10**12)
min = 10
max = 0
while (p>0):
    
    k = p%10
    max = max(h, max)
    min = min(h, min)
    p //= 10
print((max+min)**2)
