print(45, 36, 28, sep='', end='')
print("Paata")
print("Mamporia")


##s = 0
##s = s + 1    # s += 1
##print(s)
##
##s += 1
##print(s)
##
##
##s **= 2
##print(s)


numb = int(input("Enter an integer number: "))   # 584
reverse_numb = 0

while numb:    # 584  58  5
  reverse_numb = reverse_numb * 10 + numb % 10  # 4  4*10+8=48  48*10+5=485
  numb //= 10    # 58   5  0

print(reverse_numb)
