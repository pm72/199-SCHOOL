x = int(input("Enter an integer number: "))    # 8593

reverse_x = 0
while x:    # 8593   859   85  8  0
  reverse_x = reverse_x * 10 + x % 10  # 3 3*10+9=39 39*10+5=395 395*10+8= 3958

  x //= 10   # 859  85  8  0

print("Reverse number is", reverse_x)
