import math
import random

x1 = random.randint(1,10000000)
x2 = random.randint(1,10000000)
y1 = random.randint(1,10000000)
y2 = random.randint(1,10000000)

a = (x2-x1) ** 2
b = (y2-y1) ** 2

print(math.sqrt((a+b)))


