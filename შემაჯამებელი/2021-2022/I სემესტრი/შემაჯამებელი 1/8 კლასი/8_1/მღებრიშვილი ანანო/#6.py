import random
x = random.randint(10**11, 10**12)
ab = 10
ac = 0
while (x > 0):
    y = x % 10
    ac = max(y, ac)
    ab = min(y, ab)
    x //= 10
print((ac + ab) ** 2)
