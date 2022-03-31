# სტრიქონები  strings

# a = "This is a string."
# print(a)
#
# a = 'This is a string.'
# print(a)
#
# a = "d"
# print(a, type(a))
#
# a = '12345'
# print(a, type(a))
#
# a = 12345
# print(a, type(a))


# მრავალსტრიქონიანი სტრიქონები
# intro = "Hello there! \
# My name is Paata Mamporia, \
# I am 49 years old. \
# I love Rugby."
# print(intro)
#
# intro = "Hello there! " \
#         "My name is Paata Mamporia, " \
#         "I am 49 years old. " \
#         "I love Rugby."
# print(intro)
#
# print()
#
# # '\n'   ახალ ხაზზე გადასვლა  New line  End line   ENTER
# intro = "Hello there!\n\
# My name is Paata Mamporia,\n\
# I am 49 years old.\n\
# I love Rugby."
# print(intro, "\n")
#
#
# intro = """Hello there!
# My name is Paata Mamporia,
# I am 49 years old.
# I love Rugby."""
# print(intro, "\n")
#
#
# intro = '''Hello there!
# My name is Paata Mamporia,
# I am 49 years old.
# I love Rugby.'''
# print(intro, "\n")
#
#
# intro = '''Hello there!
#             My name is Paata Mamporia,
#                       I am 49 years old.
#         I love Rugby.'''
# print(intro, "\n")


# ბრჭყალები ბრჭყალებში
# "Hello", said Susan.
# print('"Hello", said Susan.')
# print("'Hello', said Susan.")
#
# # "That's my Teddy", said Pedro.
# print("\"That's my Teddy\", said Pedro.")
# print('"That\'s my Teddy", said Pedro.')
# print(""""That's my Teddy", said Pedro.""")
# print('''"That's my Teddy", said Pedro.''')
# print("c:\\user\\paata\\strings.py")
# print(r"c:\user\paata\strings.py")
# print(r"c:\user\paata\strings.py\n")


# სტრიქონების შეწებება '+' ოპერატორით (სტრიქონების კონკატებაცია)
# str1 = "Hello"
# str2 = "there"
# string = str1 + ' ' + str2 + "!"
# print(string)
#
# # Susan sais "Hi"!
# a = 'Hi'
# print('Susan sais "' + a + '"!')


# წვდომა სტრიქონის სიმბოლოებზე
# a = 'Hello there!'
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[11], "\n")
#
# print(a[-1])
# print(a[-2])
# print(a[-3])


# ჭრები სტრიქონში Slice. სინტაქსი: string[start:stop:step]
# a = 'Hello there!'
# print(a[0:4])       # პირველი ოთხი სიმბოლო
# print(a[:4])        # პირველი ოთხი სიმბოლო
# print(a[2:7])       # სიმბოლოები მითითებული დიაპაზონით
# print(a[2:9:3])     # სიმბოლოები მითითებული დიაპაზონით
# print(a[3:])
# print(a[-4:])       # ბოლო ოთხი სიმბოლო
# print(a[-7:-3])

# a = "Hello there!"
# print(a, id(a))



# სტრიქონული მეთოდები

#1. სტრიქონის სიგრძე (სიმბოლოების რაოდენობა)
# len()
# a = "Hello there!"
# print(len(a))


#2. .capitalize(), .upper(), .lower(), .title()
# სინტაქსი: string.capitaliz(), string.upper(), ...
# a = "i aM herE."
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.title())
# print(a[:3].upper() + a[3:].lower())


#3. .count()
# სინტაქსი: string.count(word)
# a = '''Susan is a lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan.'''
# print(a.count('Susan'))
# print(a.count('Barky'))
# print(a.count('barky'))


#4. .strip(), .lstrip(), .rstrip()
# a = "               Hello there!          "
# a = a.strip()
# print(a)
#
# a = "               Hello there!          "
# a = a.lstrip()
# print(a)
#
# a = "######numbers: 123, numbers: 456!!!!"
# a = a.strip('#')
# a = a.strip('!')
# print(a.strip('#'))
# print(a)


#5. .replace(), .find(), index()
# a = '''Susan is a lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan.'''
#
# a = a.replace('Susan', 'Ronny', 1)
#
# print(a)

# a = 'I cyan love coding. I have fun with coding.'
# print(a.find('coding', 2))
# print(a.find('Coding'))
#
# s = a.find('coding') + len('coding')
# print(s)
# print(s + a[s:].find('coding'))


#6. .isalnum(), .isalpha(), isnumeric()  <=======>  True / False   (ჭეშმარიტი / მცდარი)
# a = "numbers123numbers456"
# b = "numbers 58790"
# print(a.isalnum())
# print(b.isalnum())

# a = "PaataMamporia"
# b = "Paata Mamporia"
# print(a.isalpha())
# print(b.isalpha())

# a = "123589710256"
# b = "5..69"
# print(a.isnumeric())
# print(b.isnumeric())

#7. .islower(), .isupper(), .istitle()
# a = "paata mamporia is 49 years old."
# b = "Paata mamporia is 49 years old."
# print(a.islower())
# print(b.islower())

# a = "PAATA MAMPORIA"
# b = "Paata mamporia is 49 years old."
# print(a.isupper())
# print(b.isupper())

# a = "paata mamporia is 49 years old."
# b = "Paata Mamporia Is 49 Years Old."
# print(a.istitle())
# print(b.istitle())


#8. სტრიქონების ფორმატირება
# a = 14
# b = 5.13
# # Result: 4 + 5 = 9
#
# print("Result:", a, "/", b, "=", a / b)
# print("Result:", a, "/", b, "=", round(a / b, 2))
# print("Result:", a, "/", b, "=", round(a / b, 3))
# print("Result:", a, "/", b, "=", round(a / b, 4))
#
# # f-სტრიქონები   f-string    f"sds adada {} {} {}"
# print("Result: a / b = a/b")
# print("Result: {a} / {b} = {a/b}")
# print(f"Result: {a} / {b} = {a/b}")
# print(f"Result: {a} / {b} = {round(a/b, 2)}")
# print(f"Result: {a} / {b} = {(a / b):.3f}")
# print(f"Result: {a} / {b} = {(a / b):10.3f}")
#
# # შაბლონები  Templates   "{} {} ... {}".format(arg1, arg2, ..., argN)
# print("Result: {} / {} = {:.2f}".format(a, b, a/b))

result = "Result: {} / {} = {:.2f}"

x = 45
y = 8.95
print(result.format(x, y, x/y))
print(result.format(x, y, x/y, 58))