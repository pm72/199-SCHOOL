import random
x = random.randrange(100, 1000)  # x = random.randint(100, 999)
# print(x, " ", int(x/60), " ", x-int(x/60)*60)
print(x, x // 60, x % 60)


input()