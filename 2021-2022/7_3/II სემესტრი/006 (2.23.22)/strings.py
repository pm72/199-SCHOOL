# სტრიქონები   string

# a = "This is a string"
# print(a)
#
# a = "d"
# print(a, type(a))
#
# a = 'd'
# print(a, type(a))
#
# a = '123456'
# print(a, type(a))
#
# a = 123456
# print(a, type(a))
#
# a = 1234.56
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
# print(intro)
#
# print()
#
# # '\n'  ===> ახალ ხაზზე გადასვლა  ENTER
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
# intro = '''Hello there!
# My name is Paata Mamporia,
# I love Rugby.'''
# print(intro, "\n")
#
# intro = '''Hello there!
# My name is Paata Mamporia,
# I love Rugby.'''
# print(intro, "\n")
#
# intro = '''Hello there!
#     My name is Paata Mamporia,
#                 I love Rugby.'''
# print(intro, "\n")


# ბრჭყალები ბრჭყალებში
# "Hello", said Susan
# print("\"Hello\", said Susan")
# print('"Hello", said Susan')
# print("'Hello', said Susan")
#
# # "That's my Teddy", said Pedro
# print("\"That's my Teddy\", said Pedro")
# print('"That\'s my Teddy", said Pedro')
#
# print("c:\\user\\paata\\strings.py")
# print(r"c:\user\paata\strings.py")
# print(r"c:\user\paata\strings.py\n")


# სტრიქონების მიბმა '+' ოპერატორით (კონკატენაცია)
# str1 = 'Hello'
# str2 = 'there'
# string = str1 + ' ' + str2 + "!"
# print(string)
#
# string = str2 + ' ' + str1 + "!"
# print(string)
#
# # Susan sais "Hi"
# a = 'Hi'
# print('Susan sais "' + a + '"!')
# print('Bob sais "' + a + '"!')


# სტრიქონული მეთოდები

#1. სტრიქონის სიგრძე len(). სინტაქსი: len(string)
# a = "Hello there!"
# print("Length of string:", len(a))
# print("Length of typed string:", len("12354 is string's numbers"))

#2. მეთოდები .capitalize(), .upper(), .lower(), .title()
# სინტაქსი: string.capitalize(), string.upper()
# a = 'i am heRE!'
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
# Barky plays with Susan'''
# print(a.count('Susan'))
# print(a.count('Barky'))
# print(a.count('barky'))


#4. .strip(), .lstrip(), .rstrip()
# a = "   I love coding.    "
# a = a.strip()
# print(a)
#
# a = "***I love coding.********"
# print(a.rstrip('*'))
#
# a = "____I love coding.********"
# a = a.strip('_')
# a = a.strip('*')
# print(a)


#5. .replace(), .find(), index()
# a = '''Susan is a lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan.'''
#
# a = a.replace('Susan', 'Ronny')
# print(a)

a = "I love coding. I have fun with Python coding."
# print(a.find('coding'))
# print(a.find('c'))
#
# ind = a.find('coding')
# print(a[ind:ind+len('coding')])
# print(a.find('Coding'))

print(a.index('coding'))
print(a.index('Coding'))


# ჭრები არ ამიხსნია
