numb = int(input("Enter an integer number: "))   # 4832
reverse_numb = 0

while numb:  # 4832  483  48 4 0
  reverse_numb = reverse_numb * 10 + numb % 10  # 2, 2*10+3=23, 23*10+8=238
                                                # 238*10+4= 2384

  numb //= 10  # 483  48 4 0


print(reverse_numb)
print(reverse_numb * 10)
