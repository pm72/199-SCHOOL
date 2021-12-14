import random
x = random.randint(10**11, 10**12)
print(x)
minimum = 10
maximum = 0
while x>0:
    y = x%10
    maximum = max(y, maximum)
    minimum = min(y, minimum)
    x //= 10
print((maximum + minimum)**2)
