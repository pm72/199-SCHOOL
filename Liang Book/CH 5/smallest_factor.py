# Using break statment
w = 35
print("Using break statment".center(w))
print()

n = int(eval(input("Enter an integer >= 2: ")))
factor = 2

while factor <= n:
  if n % factor == 0:
    break

  factor += 1

print(f"The smallest factor then 1 for {n} is {factor}\n\n")


# Using without break statment
print("Using without break statment".center(w))
print()

##n = int(eval(input("Enter an integer >= 2: ")))
factor = 2
found = False

while factor <= n and not found:
  if n % factor == 0:
    found = True
  else:
    factor += 1

print(f"The smallest factor then 1 for {n} is {factor}\n\n")
