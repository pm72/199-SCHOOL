import random
x=random.randint(10**11,10**12)
mn=10
mx=0
while(x>0):
    t=x%10
    mx=max(t,mx)
    mn=min(t,mn)
    x//=10
print((mx+mn)**2)
