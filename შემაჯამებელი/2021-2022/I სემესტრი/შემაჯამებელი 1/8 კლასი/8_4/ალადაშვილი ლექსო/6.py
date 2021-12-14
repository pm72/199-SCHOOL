import random
a = random.randint(10**11, 10**12)
b = 10
c = -1
print(a)
while (a>0):
    t = a%10
    c = max(t,c)
    b = min(t,b)
    a //= 10
print((c+b)**2)
