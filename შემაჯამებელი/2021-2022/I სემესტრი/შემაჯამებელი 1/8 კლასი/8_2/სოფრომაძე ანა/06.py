import random

num = str(random.randint(10 ** 11, 10 ** 12 - 1))

print("Random Number: ", num)

min = max = 0


3214

for n in num:
    n = int(n)
    if (n > max):
        max = n
    elif (n < min):
        min = n

sum = (min + max) ** 2

print("Max: {}, Min: {}, Sum: {}".format(max, min, sum))
