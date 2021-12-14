import math
import random
x1=random.randint(0,10000000000)
x2=random.randint(0,10000000000)
y1=random.randint(0,10000000000)
y2=random.randint(0,10000000000)
z1=math.pow(x2-x1,2)
z2=math.pow(y2-y1,2)
z3=math.sqrt(z1+z2)
print(z3)
