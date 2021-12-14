import random
random = random.randint(10**11, 10**12)
miin = 10
maax = 0
while (random>0):
 second = random%10
 maax = max(second, maax)
 miin = min(second, miin)
 random //= 10
print((maax+miin)**2)
