import random
x = random.randint(10**11, 10**12)
pq = 10
pa = 0
while (x>0):
    r = x%10
    pa = max(r, pa)
    pq = min(r, pq)
    x //= 10
print ((pa+pq)**2)
