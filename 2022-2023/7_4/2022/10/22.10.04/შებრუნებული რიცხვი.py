numb = int(input("Enter an integer: "))   # 8593
r_numb = 0

while numb:   # 8593  859  85  8  0
##  r_numb = r_numb * 10 + numb % 10
                                    # 3  3*10+9=39  39*10+5=395  395*10+8= 3958
  r_numb *= 10
  r_numb += numb % 10
  
  numb //= 10  # 859  85  8  0


print(r_numb)
