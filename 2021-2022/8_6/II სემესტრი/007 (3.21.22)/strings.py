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

# a = '''Susan is lovely girl.
# Barky is Susan's friend.
# Barky plays with Susan.'''
#
# print(a.count('Susan'))
# print(a.count('Barky'))
# print(a.count('barky'))

#2. .strip(), rstrip(), lstrip()
# a = "   Hello there!     "
# print(a.strip())
# print(a)

#3. .replace(), .find(), index()
# a = '''Susan is lovely girl.
# Barky is Susan's friend.
# Barky plays with Susan.'''
# print(a.replace('Susan', 'Ronny'))

# a = 'I love coding. I have fun with coding.'
# print(a.find('coding'))
# print(a.find('Coding'))
# print(a.index('coding'))
# print(a.index('Coding'))

#4. .split(). სინტაქსი: string.split(separator, limit)
# a = 'I love coding.'
# print(a.split())   # ' ', '\t', '\n'
#
# a = 'I love coding.\nI have fun\t\twith coding.'
# print(a.split())   # ' ', '\t', '\n'
# print(a)

# a = 'I love coding.\nI have fun\t\twith coding.'
# print(a.split('.'))

# a = 'number#123#number#123'
# print(a.split('#'))
# print(a.split('#', 1))
# print(a.split('#', 2))

#5. ოპერატორი in  True ან False  (ჭეშმარიტი / მცდარი)
# a = "Barky is Ronny's best friend"
# print('best friend' in a)
# print('Best friend' in a)

#6. .isalnum()  ---> სტრიქონში მხოლოდ ციფრები ან ასოებია ან ორივე ერთად
# print("number123number456".isalnum())
# print("number 123 number456".isalnum())

#7. .isalpha()  ---> პოულობს სტრიქონში ანბანის ასოებს და აბრუნებს ან True-ს ან Fals-ს.
# print("PaataMamporia".isalpha())
# print("Paata Mamporia".isalpha())

#8. .isnumeric()
# print('5871023'.isnumeric())
# print('587102.3'.isnumeric())

#9. .islower(), isupper(), istitle()
# a = 'paata mamporia is a teacher.'
# print(a.islower())
#
# a = 'PAATA MAMPORIA IS A TEACHER.'
# print(a.isupper())
#
# a = 'Paata Mamporia Is A Teacher.'
# print(a.istitle())


# სტრიქონების ფორმატირება
# 4 + 5 = 9
a = 14
b = 5

print(a, '+', b, '=', a+b)

# f-სტრიქონი  f-string
print("{a} + {b} = {a+b}")
print(f"{a} + {b} = {a+b}")

print()

print(f"{(2/3):.2f}")
print(f"{(2/3):20.2f}")

a = 1.58
b = 2.96
print(f"განაყოფი: {a} / {b} = {a / b}")
print(f"განაყოფი: {a} / {b} = {(a / b):.2f}")
print(f"{0.1} + {0.1} + {0.1} = {0.1+0.1+0.1}")
print(f"{0.1} + {0.1} + {0.1} = {(0.1+0.1+0.1):.2f}")

c = round(a / b, 2)
print(c)
print(a / b)

message = f"სტრიქონის ფორმატირება: გამაყოფის დამრგვალება მესედამედე: {a} / {b} = {(a / b):.2f}"

print(message)

a = 98
b = 112
message = f"სტრიქონის ფორმატირება: გამაყოფის დამრგვალება მესედამედე: {a} / {b} = {(a / b):.2f}"
print(message)