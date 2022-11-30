print(1, 2)
print(3, 4)

print()

print(1, 2, end=' ')    # 1, 2,
print(3, 4)             # 1, 2, 3, 4
print(5, 6)             # 5, 6


print()

print('AAA', end = ' ')     # AAA 
print('BBB', end='')        # AAA BBB
print('CCC', end='***')     # AAA BBBCCC***
print('DDD', end='***')     # AAA BBBCCC***DDD***


print("\n")


import math as m

r = 3
print("The length of circle is", round(2 * m.pi * r, 2), end=' ')
print("and the area is", round(m.pi * r ** 2, 2))
print("OK \n")
