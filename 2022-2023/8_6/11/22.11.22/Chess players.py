w1 = 20
w2 = 3
w3 = 3 * w1 + 2 * w2 + len("age")
line = '-'

print(f"{' ':<{w2}s}{'Player':<{w1}s}{'Country':<{w1}s}{'Rating':<{w1}s}{'Age'}")
print(line * w3)
