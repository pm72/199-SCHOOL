##print("a    b    a ** b")
##print("1    2    1")
##print("3    4    81")
##print("4    5    1024")
##print("5    6    15625")
##
##
##

x = int(input("Enter number: "))

reverse_x = 0


while x:
    reverse_x = reverse_x * 10 + x % 10

    x //= 10


print(reverse_x)
