import random
x=random.randint(10**11,10**12)
y=10
z=0
while(x>0):

   n=x%10
   z=max(n,z)
   y=min(n,y)
   x//10
print((z+y)**2)
