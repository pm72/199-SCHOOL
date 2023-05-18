# prime number

number = int(eval(input("Enter a number: ")))
divisor = 2

while divisor <= number ** 0.5:
  if number % divisor == 0:
    print(f"{number} isn't prime")
    break

  divisor += 1
else:
  print(f"{number} is prime")
