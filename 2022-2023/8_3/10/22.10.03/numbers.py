x = int(input("Enter an integer number: "))   # 5894  589  58  5

reverse = 0
while x:
  reverse = reverse * 10 + (x % 10)
  x //= 10



print(reverse)
