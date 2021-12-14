from random import randint
num = randint(100, 999)
mins = num // 60
secs = num % 60
print(num, mins, secs)
