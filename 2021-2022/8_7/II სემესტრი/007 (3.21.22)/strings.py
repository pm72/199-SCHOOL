# სტრიქონი  string

# a = "This is a string"
# print(a)
#
# a = 'This is a string'
# print(a)
#
# b = "d"
# print(b, type(b))
#
# numbers = '1234'
# print(numbers, type(numbers))


# მრავალსტრიქონიანი სტრიქონი
# intro = "Hello there! \
# My name is Paata Mamporia, \
# I love Rugby!"
#
# print(intro, "\n")     # \n  -   ENTER
#
# intro = "Hello there!\n\
# My name is Paata Mamporia,\n\
# I love Rugby!"
#
# print(intro, "\n")
#
# intro = "Hello there" \
#         "My name is Paata Mamporia" \
#         "I love Rugby"
# print(intro, "\n")
#
# intro = """Hello there!
# My name is Paata Mamporia,
# I love Rugby!"""
# print(intro, "\n")
#
# intro = \
# '''Hello there!
#     My name is Paata Mamporia,
#         I love Rugby!'''
# print(intro)


# ბრჭყალები სტრიქონში
# # "Hello there", said Susan
# print('"Hello there", said Susan')
# print("'Hello there', said Susan")
#
# print()
#
# # "That's my Taddy", said Pedro
# print("\"That's my Taddy\", said Pedro")
# print('"That\'s my Taddy", said Pedro')
# print(""""That's my Taddy", said Pedro""")
# print('''"That's my Taddy", said Pedro''')
# print("c:\\user\\paata\\strings.py")
# print(r"c:\user\paata\strings.py")
# print(r"c:\user\paata\strings.py\n")
# print("c:\\user\\paata\\strings.py\n")


# სტრიქონების კონკატენაცია
# str1 = "Hello"
# str2 = "there!"
# string = str1 + " " + str2
# print(string)
#
# print()
#
# # Susan sais 'Hi'
# a = 'Hi'
# print("Susan sais '" + a + "'")


# ცარიელი სტრიქონი
# a = ''
# a = ""
# print(a)


# წვდომა სტრიქონის სიმბოლოებთან
# a = "Hello there!"
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[11])
# print(a[-1])
# print(a[-2])
# print(a[-3])


# ჭრები სტრიქონში  slice
# a = "Hello there!"
#
# print(a[0:4])     # პირველი ოთხი სომბოლო
# print(a[:4])      # პირველი ოთხი სომბოლო
# print(a[7:12])    # სიმბოლოები მოცემული დიაპაზონით
# print(a[-4:])     # ბოლო ოთხი სომბოლო
#
# print()
# print(a)

# a = "Hello there!"
# print(a, id(a))
#
# a = a[:6] + 'friends!'
# print(a, id(a))
#
# a = 't' + a[1:]
# print(a, id(a))


# სტრიქონული მეთოდები
# სტრიქონის სიგრძე  len()    len(string)
# a = "Hello there!"
# print(len(a))


# .capitalize(), .upper(), .lower(), .title()
# a = "i am here!"
# print(a.capitalize())
# print(a.upper())
#
# a = "I AM Here!"
# print(a.lower())
#
# a = "i love rugby!"
# print(a.title())
# print(a)


#1. .count()
# სინტქასი: string.count(word)
# a = '''Susan is a lovely girl.
# Burky is Susan's friend.
# Burky plays with Susan.'''
# print(a.count('Susan'))
# print(a.count('Burky'))
# print(a.count('burky'))
# print(a.count('susan'))

#2. strip(),  .rstrip(), .lstrip()
# a = "     I love coding.    "
# print(a)
# print(a.strip())

#3. .replace(), .find(), .index()
# a = '''Susan is a lovely girl.
# Burky is Susan's friend.
# Burky plays with Susan.'''
# print(a.replace('Susan', 'Ronny'))

# a = 'I love coding. I have fun with coding.'
# print(a.find('coding'))
# print(a.find('Coding'))
# print(a.index('coding'))
# # print(a.index('Coding'))
# print(a.index('c'))

#4. .split()
# სინტაქსი: string.split(separator, limit)
# a = 'I love coding.'
# print(a.split())    # separator=' ', separator='\t', separator='\n',

# a = 'I love coding.\nI have fun\t\twith coding!'
# print(a)
# print(a.split())    # separator=' ', separator='\t', separator='\n',

# a = 'I love coding.\nI have fun\t\twith coding!'
# print(a)
# print(a.split('.\n'))    # separator=' ', separator='\t', separator='\n',

# a = "2+3= 8 9 6 5"
# a = a.split()
# print(a)
# print(a[0])
# print(eval(a[0][:-1]))
# print(eval('1.1 == 3.3'))

# ოპერატორი 'in'
# print('coding' in 'A love coding.')     # True
# print('Coding' in 'A love coding.')     # False

# მეთოდები .isalnum(), .isalpha(), isnumeric()
# a = "number123number456"
# print(a.isalnum())

# a = "The numbers: 123456"
# print(a.isalnum())
#
# a = "Paata Mamporia"
# print(a.isalpha())
#
# a = "PaataMamporia"
# print(a.isalpha())
#
# a = "45689"
# print(a.isnumeric())
#
# a = "45.689"
# print(a.isnumeric())


# მეთოდები .islower(), .isupper(), istitle()
# a = "paata mamporia"
# b = "Paata"
# print(a.islower())
# print(b.islower())

# a = "paata mamporia"
# b = "PATTA"
# print(a.isupper())
# print(b.isupper())

# a = "paata mamporia"
# b = "Paata Mamporia"
# print(a.istitle())
# print(b.istitle())


# სტრიქონის ფორმატირება
# a = 14
# b = 5
#
# # 4 + 5 = 9
# print(a, "+", b, "=", a + b)
#
# # f-სტრიქონი   f-string
# print("{a} + {b} = {a+b}")
# print(f"{a} + {b} = {a+b}")
#
# a = 25
# b = 12
# message = f"ორი როცხვის ჯამი: {a} + {b} = {a+b}"
# print(message)
#
#
# a = 5.85
# b = 1.51
# print(message)

x = 2
y = 3
print(x / y)
print(f"განაყოფი: {x} / {y} = {x / y}")
print(f"განაყოფი: {x} / {y} = {(x / y):.2f}")
print(f"{0.1} + {0.1} + {0.1} = {0.1 + 0.1 + 0.1}")
print(f"{0.1} + {0.1} + {0.1} = {(0.1 + 0.1 + 0.1):.2f}")

z = round(0.1 + 0.1 + 0.1, 2)
print(z)

div = round(x/y, 2)
print(div)