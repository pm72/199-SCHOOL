x=(int(eval(input('sheiyvanet ricxvi 12 ciprit:'))))
x_1=x

max1=0
while x > 0:
    y=x%10
    if y>max1:
      max1=y
    x//=10
print(max1)


min1=9
while x_1 > 0:
    z=x_1%10
    if z<min1:
      min1=z
    x_1//=10
print(min1)

print((max1+min1)**2)
