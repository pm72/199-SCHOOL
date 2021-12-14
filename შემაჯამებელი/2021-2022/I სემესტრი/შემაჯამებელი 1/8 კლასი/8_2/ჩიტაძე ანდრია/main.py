'''
andria chitidze
klasi: 8²
'''

# amocana 1
print((9.5 * 4.5 - 2.5 * 3) / (45.5 - 3.5))

# amocana 2
e1 = 14
e2 = 45.5
e3 = e2 / 60
e4 = 14 / 1.6

print(f"{e4}/{e3}")

# amocana 3
from random import randint

NUM = randint(100, 999)
MINS = NUM // 60
SECS = NUM % 60
print(NUM, MINS, SECS)

# amocana 4
p = 2.59
q = -8.92
v = 2 * q / p ** q
z = (p - 2 * q) / v ** 2
x = (2.79 * p + 3 * v) / (q ** 2 - 2 * p * z)
j = 4 / 3 * (x + 34) - 9 * (p + q * z) + (3 + v * (2 + p)) / (p + q * v)
print(j)

# amocana 5
from math import sqrt

f = int(input("f = "))
n = int(input("n = "))
l = int(input("l = "))
g = int(input("g = "))
h = sqrt((n - f) ** 2 + (l - g) ** 2)
print(h)

# amocana 6
from random import randint

e = randint(100000000000, 999999999999)
e = str(e)
ans = max([int(i) for i in e]) + min([int(i) for i in e])
print(ans ** 2)
