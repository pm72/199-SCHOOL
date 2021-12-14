#6
import random
x=random.randint(10**11, 10**12)
z=0
y=10
print(x)
while (x>0):
    k = x%10
    z = max(k, z)
    y = min(k, y)
    x//=10
print((z+y)**2)
