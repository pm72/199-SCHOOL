import random
import math
x1 = random.randrange(1, 101)
x2 = random.randrange(1, 101)
y1 = random.randrange(1, 101)
y2 = random.randrange(1, 101)

mandzili = math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

print( mandzili )
