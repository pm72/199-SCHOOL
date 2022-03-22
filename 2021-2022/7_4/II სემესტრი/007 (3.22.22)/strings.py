# სტრიქონები   string

# a = "This is a string"
# print(a)
#
# numbers = '12345'
# print(numbers, type(numbers))


# მრავალსტრიქონიანი სტრიქონები
# intro = "Hello there! \
# My name is Paata Mamporia, \
# I love Rugby."
# print(intro)
#
# intro = "Hello there! " \
#         "My name is Paata Mamporia, " \
#         "I love Rugby"
# print(intro, "\n")
#
# intro = "Hello there!\n\
# My name is Paata Mamporia,\n\
# I love Rugby"
# print(intro, "\n")
#
# intro = """Hello there!
# My name is Paata Mamporia,
# I love Rugby"""
# print(intro, "\n")
#
# intro = '''Hello there!
# My name is Paata Mamporia,
# I love Rugby'''
# print(intro, "\n")
#
# intro = '''Hello there!
#       My name is Paata Mamporia,
#             I love Rugby'''
# print(intro, "\n")


# ბრჭყალები ბრჭყალებში
# # "Hello!", said Susan
# print('"Hello!", said Susan')
# print("'Hello!', said Susan")
#
# print()
#
# # "That's my Taddy", said Pedro.
# print("\"That's my Taddy\", said Pedro.")
# print('"That\'s my Taddy", said Pedro.')
# print(""""That's my Taddy", said Pedro.""")
# print('''"That's my Taddy", said Pedro.''')
#
# print()
#
# print("c:\\users\\paata\\strings.py")
# print(r"c:\users\paata\strings.py")
# print(r"c:\users\paata\strings.py\n")


# სტრიქონების კონკატენეაცია
# str1 = "Hello"
# str2 = "there"
# string = str1 + ", " + str2 + "!"
# print(string, "\n")
#
# # Susan sais "Hi"
# a = 'Hi!'
# print('Susan sais "' + a + '"')


# ცარიელი სტრიქონი
# a = ''
# a = ""
# print(a, type(a))


# წვდომა სტრიქონის ელემენტებთან
# a = 'Hello there!'
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[11], "\n")
#
# print(a[-1])
# print(a[-2])
# print(a[-3])


# ჭრები სტრიქონში  Slice
# a = 'Hello there!'
# print(a[0:4])           # პირველი ოთხი სიმბოლი
# print(a[:4])            # პირველი ოთხი სიმბოლი
# print(a[5:9])           # სიმბოლოები მითითებული დიაპაზონით
# print(a[2:9:3], "\n")   # სიმბოლოები მითითებული დიაპაზონით
#
# print(a[-4:])           # ბოლო ოთხი სიმბოლო
# print(a[6:])
# print(a[-9: -3])

# a = "Hello there!"
# print(a, id(a))
#
# a = 'T' + a[1:]
# print(a, id(a))
#
# a = 'H' + a[1:]
# print(a, id(a))


# სტრიქონული მეთოდები

#1. სტრიქონის სიგრძე len().   სინტაქსი: len(string)
# a = "Hello there!"
# print(len(a))

#2. მეთოდები .capitalize(), .upper(), .lower(), .title()
# სინტაქსი: string.capitalize(), string.upper()
# a = 'i am here!'
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.title())
#
# print()
# print(a)


#3. .count()
# სინტაქსი: string.count(word)
# a = '''Susan is a lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan.'''
# print(a.count('Susan'))
# print(a.count('Barky'))
# print(a.count('susan'))


#4. .strip(), .lstrip(), .rstrip()
# a = "    I love coding.          "
# a = a.strip()
# print(a)
#
# a = '___numbers 1234 numbers 5678#############'
# a = a.strip('_')
# a = a.strip('#')
# print(a)


#5. .replace(), .find(), .index()
# a = '''Susan is a lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan.'''
# a = a.replace('Susan', 'Ronny')
# print(a)

# a = "I love coding. I fun with coding."
# print(a.find('coding'))
# print(a.find('Coding'))
#
# print(a.index('coding'))
# print(a.index('Coding'))


#6. .split()
# სინტაქსი: string.split(separator, limit)
# a = "I love coding."
# print(a.split())   # separator=' ' and separator='\n' and separator='\t', limit=inf
#
# a = "I love coding.\nI have fun with\t\t\tPython coding"
# print(a.split())   # separator=' ' and separator='\n' and separator='\t', limit=inf
#
# a = 'i love coding.\nI fun\t\twith coding.'
# print(a.split('.'))
#
# a = 'i love coding.\nI fun\t\twith coding.'
# print(a.split('.\n'))
#
# print("numbers#123#numbers#456".split('#'))
#
# a = "2+3=;8;5;9;1"
# print(a.split(';'))


#7. ოპერატორი 'in'   ====>  True / False (შეშმარიტი / მცდარი)
# a = "Barky is Susan's best friend."
# print('best friend' in a)
# print('Best friend' in a)
#
# substring = 'Best friend'
# string = "Barky is Susan's best friend."
# print(substring in string)


#8. .isalnum(), .isalpha(), isnumeric()
# a = "numbers123numbers456"
# b = "numbers 123"
# print(a.isalnum())
# print(b.isalnum())

# a = "PaataMamporia"
# b = "Paata Mamporia"
# print(b.isalpha())
# print(a.isalpha())

# a = "125689"
# b = "125.69"
# print(a.isnumeric())
# print(b.isnumeric())


# 9 .islower(), .isupper(), .istitle()
# a = "paata mamporia is 49 years old."
# b = "Paata mamporia is 49 years old."
# print(a.islower())
# print(b.islower())

# a = "PAATA MAMPORIA."
# # b = "Paata mamporia is 49 years old."
# # print(a.isupper())
# # print(b.isupper())

# a = "Paata Mamporia Is 49 Years Old."
# b = "Paata mamporia is 49 years old."
# print(a.istitle())
# print(b.istitle())


#10. სტრიქონის ფორმატირება
# a = 14.2
# b = 5.1
#
# # 4 + 5 = 9
#
# print(a, "/", b, "=", a / b)
#
# # f-სტრიქონი   f-string
# print("a / b = a/b")
# print("{a} / {b} = {a/b}")
# print(f"Result: {a} / {b} = {a/b}")
#
# print()
#
# print(f"Result: {a} / {b} = {(a/b):.2f}")

# a = 14.2
# b = 5.1
# result = round(a / b, 2)
#
# print(f"{a} / {b} = {result}")


# a = 4
# b = 5
# result = f"{a} + {b} = {a + b}"
# print(result)
#
# print()
#
# a = 14
# b = 52
# print(result)


# შაბლონები
# string.format(arg1, arg2, arg3, ..., argN)
result = "Result: {} + {} = {}"

a = 14
b = 56
print(result)
print(result.format(a, b, a+b))

x = 14.89
y = 1.26
print(result.format(x, y, round(x + y, 2)))