import random

#num = 500
num = random.randint(100,999)

min = num // 60
sec = num % 60

print("Minutes: {}, Seconds {}".format(min, sec))
