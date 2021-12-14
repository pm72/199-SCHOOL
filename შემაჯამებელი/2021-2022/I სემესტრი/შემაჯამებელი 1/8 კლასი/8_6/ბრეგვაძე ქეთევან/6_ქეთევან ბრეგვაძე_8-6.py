import random
r = random.randint(10**11, 10**12)
x = 10
y = 0
while (r>0):
    m = r%10
    y = max(m, y)
    x = min(m, x)
    r //= 10
print((y+x)**2)