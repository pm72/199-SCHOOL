import random
q = random.randint(10**11, 10**12)
ke = 10
ks = 0
while (q>0):
    q = q%10
    ks = max(q, ks)
    ke = min(q, ke)
    q //=10
print((ks + ke)**2)
