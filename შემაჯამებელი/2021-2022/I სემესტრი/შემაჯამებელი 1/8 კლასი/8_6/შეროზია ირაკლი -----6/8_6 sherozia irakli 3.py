from random import randint
n = randint(100, 999)
min = n // 60
sec = n - (min * 60)

print(n)
print(min)
print(sec)

input()