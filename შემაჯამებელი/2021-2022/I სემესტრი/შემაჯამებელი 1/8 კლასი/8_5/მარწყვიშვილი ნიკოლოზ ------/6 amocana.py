from random import *
from math import *
q = randint(100000000000, 999999999999 + 1)  # (1, 10**12 - 1)
umciresi = min(str(q))
udidesi = max(str(q))
umciresi = int(umciresi)
udidesi = int(udidesi)
print((umciresi + udidesi)**2)

