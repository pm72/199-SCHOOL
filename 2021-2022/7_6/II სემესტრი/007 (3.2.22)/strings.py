# სტრიქონები   string

# a = 'This is a string'
# print(a)
#
# a = "d"
# print(a)
#
# a = '12345'
# print(a, type(a))


# მრავალსტრიქონიანი სტრიქონები
# intro = "Hello there! \
# My name is Paata Mamporia, \
# I love Rugby."
# print(intro)
#
# intro = "Hello there! " \
#         "My name is Paata Mamporia, " \
#         "I love Rugby."
# print(intro, "\n")
#
# intro = "Hello there!\n\
# My name is Paata Mamporia,\n\
# I love Rugby."
# print(intro, "\n")
#
# intro = """Hello there!
# My name is Paata Mamporia,
# I love Rugby."""
# print(intro, "\n")
#
# intro = """Hello there!
#     My name is Paata Mamporia,
#             I love Rugby."""
# print(intro, "\n")
#
# intro = '''Hello there!
#     My name is Paata Mamporia,
#             I love Rugby.'''
# print(intro, "\n")


# ბრწყალები ბრჭყალებში
# # "Hello", said Susan
# print('"Hello", said Susan')
# print("'Hello', said Susan")
# print(""""Hello", said Susan""")
# print('''"Hello", said Susan''')
#
# print()
#
# # "That's my Teddy", said Pedro.
# print("\"That's my Teddy\", said Pedro.")
# print('"That\'s my Teddy", said Pedro.')
# print("c:\\user\\paata\\strings.py")
# print(r"c:\user\paata\strings.py")
# print(r"c:\user\paata\strings.py\n")


# სტრიქონების კონკატენაცია
# str1 = "Hello"
# str2 = "there!"
# string = str1 + " " +  str2
# print(string, "\n")
#
#
# # Susan sais "Hi"
# a = 'Hi'
# print('Susan sais "' + a + '"')


# ცარიელი სტრიქონი
# a = ''
# a = ""
# print(a, type(a))


# წვდომა სტრიქონის ელემენტებზე
# a = 'Hello there!'
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[11], "\n")
#
# print(a[-1])
# print(a[-2])
# print(a[-3])


# ჭრები სტრიქონში Slice. sintaqsi string[start:stop:step]
# a = 'Hello there!'
# print(a[0:4])         # პირველი ოთხი სიმბოლო
# print(a[:4])          # პირველი ოთხი სიმბოლო
# print(a[5:9])         # სიმბოლოები მითითებული დიაპაზონით
# print(a[2:9:3], "\n") # სიმბოლოები მითითებული დიაპაზონით
#
# print(a[-4:])         # ბოლო ოთხი სიმბოლო
# print(a[-11:-4])
# print(a[4:])
# print(a[4::2])
# print(a[:9:3])

# a = 'Hello there!'
# print(a, id(a))
#
# a = 'P' + a[1:]
# print(a, id(a))
#
# a = 'H' + a[1:]
# print(a, id(a))


# სტრიქონული მეთოდები

#1. სტრიქონის სიგრძე len(). სინტაქსი: len(string)
# a = 'Hello there!'
# print(len(a))

#2. მეთოდები: .capitalize(), .upper(), .lower(), .title()
# სინტაქსი: string.capitalize(), string.upper()
# a = 'i am there!'
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
# Barky plays with Susan...'''
# print(a.count('Susan'))
# print(a.count('Barky'))
# print(a.count('susan'))
# print(a.count("Susan'"))
# print(a.count('Susan\''))


#4. .strip(), .lstrip(), .rstrip()
# a = '     I love coding. I have fun with Python coding.       '
# a = a.strip()
# print(a)


#5. .replace(), .find(). index()
# a = '''Susan is a lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan...'''
# a = a.replace('Susan', 'Ronny')
# print(a)

# a = 'I love coding. I have fun with Python coding.'
# print(a.find('coding'))
# print(a.find('Coding'), "\n")
#
# print(a.index('coding'))
# print(a.index('Coding'))


#6. .split()
# სინტაქსი: string.split(separator, limit)
# a = "I love coding."
# print(a.split())   # separator=' ' and separator='\n' and separator='\t'
#
# a = "I love coding.\nI have fun with\t\t\tPython coding."
# print(a.split())   # separator=' ' and separator='\n' and separator='\t'
#
# a = "I love coding.\nI have fun with\t\t\tPython coding."
# print(a.split('.'))   # separator=' ' and separator='\n' and separator='\t'
#
# a = "I love coding.\nI have fun with\t\t\tPython coding."
# print(a.split('.\n'))   # separator=' ' and separator='\n' and separator='\t'
#
# # 3+5= 7, 6, 8, 9
# a = "3+5=;7;6;8;9"
# print(a.split(';'))


#7. ოპერატორი 'in'   ======> True / False (ჭეშმარიტი / მცდარი)
# a = "Paata is Demetre's father."
# print('Demetre' in a)
# print('demetre' in a)


#8. მეთოდები: .isalnum(), isalpha(), isnumeric()
# a = "numbers123numbers456"
# b = "numbers 123"
# print(a.isalnum())
# print(b.isalnum())

# a = "PaataMamporia"
# b = "Paata Mamporia"
# print(a.isalpha())
# print(b.isalpha())

# a = "12345689"
# b = "125.96"
# print(a.isnumeric())
# print(b.isnumeric())


#9. .islower(), .isupper(), .istitle()
# a = "paata mamporia"
# b = "Paata mamporia"
# print(a.islower())
# print(b.islower())
#
# a = "PAATA MAMPORIA"
# b = "Paata mamporia"
# print(a.isupper())
# print(b.isupper())
#
# a = "paata mamporia"
# b = "Paata Mamporia"
# print(a.istitle())
# print(b.istitle())


# სტრიქონების ფორმატირება
# a = 14.15
# b = 5.6
#
# # 4 + 5 = 9
#
# print(a, "/", b, "=", a / b)
# print(a, "/", b, "=", round(a / b, 2))
#
# # f-სტრიქონი  f-string
# print("a / b = a/b")
# print("{a} / {b} = {a/b}")
# print(f"{a} / {b} = {a/b}")
# print(f"{a} / {b} = {(a/b):.2f}")

# a = 4
# b = 5
# result = f"{a} / {b} = {a / b}"
# print(result)
# print(type(result))
#
# print()
#
# a = 14
# b = 51.23
# print(result)

# შაბლონები, ესკიზები   str.format(arg1, arg2, ..., argN)
result = "Result: {} / {} = {}"

a = 4
b = 5
print(result.format(a, b, a/b))


a = 14
b = 51.13
print(result.format(a, b, round(a/b, 2)))
print("Result: {} / {} = {}".format(a, b, round(a/b, 2)))
print("Result: {} / {} = {:.2f}".format(a, b, a / b))
print(f"Result: {a} / {b} = {(a/b):.2f}")
print("Result: ",a, "/", b, "=", round(a / b, 2))