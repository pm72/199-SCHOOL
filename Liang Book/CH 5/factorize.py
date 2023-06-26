x = int(eval(input("Enter a number: ")))
divisor = 2

print("Divisors are:\n")

while x > 1:
  if x % divisor == 0:
    print(f"{divisor:<3d}", end='')
    x //= divisor
  else:
    divisor += 1

print("\n\nDone!\n")
