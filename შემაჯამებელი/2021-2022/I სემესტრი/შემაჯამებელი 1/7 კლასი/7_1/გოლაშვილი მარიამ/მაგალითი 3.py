import random
import math
randomNumber = random.uniform(100,999)
seconds = math.floor(randomNumber)
minute= math.floor(seconds/60)
seconds2=seconds-60*minute
print(seconds,minute,seconds2)
