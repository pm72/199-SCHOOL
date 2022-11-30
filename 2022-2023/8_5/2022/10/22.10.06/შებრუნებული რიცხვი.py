x = int(input("Enter an integer: "))    # 8593

reversed_x = 0
while x:      # 8593  859  85  8   0
  reversed_x = reversed_x * 10 + x % 10 # 3 3*10+9=39
                                        # 39*10+5=395
                                        # 395*10+8= 3958
  
  x //= 10    # 859  85  8  0


print("Reversed number is", reversed_x)
