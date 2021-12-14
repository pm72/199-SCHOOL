import random
#p=random.randint(100000000000,1000000000000)
p = random.randint(1, 10**12 - 1)
r=0
b=10

while(p>0):
 h=p%10
 r=max(h, r)
 b=min(h, b)

 p//=10


print((r+b)**2)
