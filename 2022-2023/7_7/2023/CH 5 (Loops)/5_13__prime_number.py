# prime number

number = int(eval(input("Enter a number: ")))
divisor = 2

while divisor <= number ** 0.5:
  if number % divisor == 0:
    print(f"{number} isn't prime")
    print(f"The first divisor is {divisor}")
    break

  divisor += 1
else:
  print(f"{number} is prime")


# ==============
input("\n\nDone!\n")