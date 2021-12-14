import random as r

# I ვარიანტი
x = str(r.randint(1, 10**12-1))

print(x)
print((max(int(i) for i in x) + min(int(i) for i in x)) ** 2)

print()


# II ვარიანტი
x = int(x)
print(x)
min_ = max_ = x % 10
x //= 10

while(x):
    digit = x % 10
    if digit < min_:
        min_ = digit
    elif digit > max_:
        max_ = digit
    
    x //= 10

print((min_ + max_) ** 2)