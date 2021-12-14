import random 
import math


x = random.randint(100,999)

a = math.floor (x/60)
b = x%60

print(x, a, b)
