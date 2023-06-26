NUMBER_OF_PRIMES = 50
NUMBER_OF_PRIMES_PER_LINE = 10
number = 2
count = 0

print("The first 50 prime numbers:\n")

while count < NUMBER_OF_PRIMES:
  is_prime = True
  divisor = 2

  while divisor <= number ** 0.5:
    if number % divisor == 0:
      is_prime = False
      break

    divisor += 1

  if is_prime:
    count += 1

    print(f"{number:<5d}", end='')

    if count % NUMBER_OF_PRIMES_PER_LINE == 0:
      print()
      
  number += 1
