import random
a = random.randint(10**11, 10**12)
b = 10
c = 0
while (a>0):
 d = a%10
 c = max(d, c)
 b = min(d, b)
 a //= 10
print((c+b)**2)
