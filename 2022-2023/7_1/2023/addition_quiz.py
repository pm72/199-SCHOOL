import random as r

##print(r.randint(1, 9))
##print(r.randrange(1, 9))
##
##print(r.random())
##print(r.uniform(0.5, 0.6))

x = r.randint(1, 9)
y = r.randint(1, 9)

answer = int(input(f"What is {x} + {y}? "))

print(f"{x} + {y} = {answer} is {x + y == answer}")
