import random
x = random.randint(10**11, 10**12)
y = 10
z = -1
print(x)
while (x>0):
    t = x%10
    z = max(t,z)
    y = min(t,y)
    x //= 10
print((z+y)**2)


