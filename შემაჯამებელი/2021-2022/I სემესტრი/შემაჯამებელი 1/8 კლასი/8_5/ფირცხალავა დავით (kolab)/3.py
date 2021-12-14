import random
a = random.randint(100,999)

seconds = a%60
minutes = int((a - a%60)/60)

print(a,seconds,minutes)