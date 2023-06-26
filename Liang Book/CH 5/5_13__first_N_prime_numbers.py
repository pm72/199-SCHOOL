NUMBER_OF_PRIMES = 50
NUMBER_OF_PRIMES_PER_LINE = 10
number = 2
count = 0

while count < NUMBER_OF_PRIMES:
  divisor = 2

  while divisor <= number ** 0.5:
    if number % divisor == 0:
      break

    divisor += 1
  else:
    count += 1

    print(f"{number:<5d}", end='')
    
    if count % NUMBER_OF_PRIMES_PER_LINE == 0:
      print()  

  number += 1
