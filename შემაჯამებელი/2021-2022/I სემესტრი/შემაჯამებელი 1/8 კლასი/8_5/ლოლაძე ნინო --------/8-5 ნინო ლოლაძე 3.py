import random
x = random.randint (100,999)

seconds = x%60
minutes = int((x - x%60)/60)

print(x,seconds,minutes)

