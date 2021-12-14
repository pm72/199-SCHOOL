import random
a=random.randint(10**11, 10**12)
minimum=10
maximum=0
while (a>0):
    k = a%10
    maximum = max(k, maximum)
    minimum = min(k, minimum)
    a //= 10
print ((maximum+minimum)**2)
