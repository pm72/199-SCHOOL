import random
x = random.randint(100,999)
seconds = x % 60;
minute = (x - seconds)/60
print(x , minute , seconds)