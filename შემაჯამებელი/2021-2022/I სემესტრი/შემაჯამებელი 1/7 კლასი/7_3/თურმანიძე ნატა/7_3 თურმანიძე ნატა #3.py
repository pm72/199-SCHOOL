import random
import math

x = random.randint(100,999)
y = math.floor(x/60)
z = x - y*60


print(str(x) + " " + str(y) + " " + str(z))
