# factorize numbers

number = int(eval(input("enter a number: ")))
divisor = 2

while number > 1:
  if number % divisor == 0:
    print(f"{divisor:<5d}", end='')
    number //= divisor
  else:
    divisor += 1


# ==============
input("\n\nDone!\n")
