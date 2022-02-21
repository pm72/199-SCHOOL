# a = 'Hello there!'
#
# print(a[0])
# print(a[-12])
# print(a[5])
#
# # ბოლო სიმბოლოს დასაბეწდად ვიყენებთ უარყოფით ინდექსს: -1
# print(a[-1])
# print(a[-2])
#
# # a[0] = 'P'    სიმბოლოს შეცვლა სტრიქონში არ შეიძელება
#
# print()
#
# # სტრიქონობის დაჭრა  (slice)
# a = 'Hello there!'
# print(a[0:4])   # [0:3]   პირველი ოთხი სიმბოლო
# print(a[7:11])  # სიმბოლოები 7-(11-1) ინდექსით
# print(a[-4:])   # ბოლო ოთხი სიმბოლო
# print(a[:4])    # პირველი ოთხი სიმბოლო
# print(a[0:8:2]) # სიმბოლოები მოცემული დიაპაზონით
#
# print(a, id(a))
#
# a = a[:6] + 'friends!'
#
# print(a, id(a))


# ==========================
# სტრიქონული მეთოდები

# სტრიქონის სიგრძე  len()
# len(string)

# a = "Hello there!"
# print(len(a))
# print(a[len(a) - 1])
# print(a[-1])


# # მეთოდები: .capitalize(), .upper(), .lower(), .title()
# a = "i am here!"
# print(a.capitalize())
# print(a.upper())
#
# a = "I Am Here!"
# print(a.lower())
#
# a = "i am here!"
# print(a.title())


# სხვადასხვა მეთოდები

#1. .count()
# string.count(word)

a = '''Susan is lovely girl.
Barky is Susan's friend.
Barky plays with Susan.'''

print(a.count('Susan'))
print(a.count('Barky'))
print(a.count('barky'))