number = 2
count = 0
N = 50

while count < N:
    divisor = 2
    
    while divisor <= number ** 0.5:
        if number % divisor == 0:
            break
        
        divisor += 1
    else:
        count += 1
        print(f"{number:<6d}", end='')
        
        if count % 10 == 0:
            print()
    
    number += 1
