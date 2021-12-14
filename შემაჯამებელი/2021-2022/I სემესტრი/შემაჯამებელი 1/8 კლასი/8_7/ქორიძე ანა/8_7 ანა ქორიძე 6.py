import random
r=random.randint(10**11,10**12)
mc=15
mk=0
while(r>0):
    b=r%10
    mc=max(b,mk)
    mk=min(b,mc)
    r//=10
print((mc+mk)**2)
