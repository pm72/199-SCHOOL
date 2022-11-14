##print(85, 14, 96, sep='', end='')
##print("Paata")
##print("Mamporia")


numb = int(input("Enter an integer number: "))   # 8596
reverse_numb = 0

while numb:  # 8596  859  85  8   0
##  reverse_numb = reverse_numb * 10 + numb % 10
                                                # 6, 6*10+9=69, 69*10+5=695
                                                # 695*10+8 = 6958
    reverse_numb *= 10
    reverse_numb += numb % 10

    numb //= 10  # 859  85   8 0

print(reverse_numb)
