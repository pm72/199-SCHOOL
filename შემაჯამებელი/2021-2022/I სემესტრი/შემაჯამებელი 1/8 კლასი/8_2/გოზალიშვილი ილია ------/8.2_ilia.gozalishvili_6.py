from random import randint
num = randint(100000000000, 999999999999)
num = str(num)
maxi = max(num)
mini = min(num)
ans = int(maxi)+int(mini)
print(num)
print(maxi, mini)
print(ans ** 2)
