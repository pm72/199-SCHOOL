import random
x = random.randrange(100000000000,999999999999)
print(x)
maxi = 0
mini = 10
while x > 0:
    maxi = max(maxi, x % 10)
    mini = min(mini, x % 10)
    x = x // 10

a = mini+maxi
ans = pow(a, 2)
print(ans)


