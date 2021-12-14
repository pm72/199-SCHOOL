# 6
import random
n = random.randint(10**11 , 10**12)
minimal = 11
maximum = 0
print(n)
while (n>0):

    nm = n % 10
    maximum = max(nm,maximum)
    minimal = min(nm, minimal)
    n = n//10

print((maximum + minimal) ** 2)