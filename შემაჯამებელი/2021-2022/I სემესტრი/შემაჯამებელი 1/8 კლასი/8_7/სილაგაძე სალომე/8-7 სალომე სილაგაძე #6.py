import random
l= random.randint(10**11, 10**12)
kp= 10
ky= 0
while (l>0):
    d=l%10
    ky = max(d,ky)
    kp = min(d,kp)
    l//= 10
print((ky+kp)**2)
