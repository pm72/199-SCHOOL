data = -1
s = 0
i = 0

while data != 0:
  i += 1
  data = eval(input())

  if data != 0:
    print(data, end= '  ')

  s += data

if s != 0:
  print(f"\n\nThe Average is {(s / (i - 1)):.2f}")
else:
  print("\n\nDivision by ZERO!!!")


''' command promt   cmd
კლავიშები:
  WIN + R   ===> cmd გაშვება

  dir   ===> ფაილების და საქაღალდეების დათვალიერება
  d:    ===> D დისკზე გადასვლა
  cd D:\199\7_3\2023\CH 5 (Loops)  ====> საქაღალდეში გადასვლა

'''
