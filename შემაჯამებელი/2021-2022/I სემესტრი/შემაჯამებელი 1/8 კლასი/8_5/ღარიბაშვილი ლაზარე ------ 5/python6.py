##6
import random
a = random.randint(10**11, 10**12)
lowest = 10
high = 0
while (a>0):
k = a%10
high = max(k, high)
lowest = min(k, lowest)
a //= 10
print((high+low)**2)