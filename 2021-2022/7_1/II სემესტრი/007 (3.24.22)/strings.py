# სტრიქონები  string

# a = "This is a string."
# print(a)
#
# a = 'This is a string.'
# print(a)
#
# a = "s"
# print(a, type(a))
#
# a = '12345'
# print(a, type(a))
#
# a = 123.45
# print(a, type(a))


# მრვალსტრიქონიანი სტრიქონები
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

# print()

# '\n'  ახალ ხაზზე გადასვლა   New line  End line  ENTER
# intro = "Hello there!\n\
# My name is Paata Mamporia,\n\
# I am 49 years old.\n\
# I love Rugby."
# print(intro, "\n")
#
# intro = 'Hello there!\n\
# My name is Paata Mamporia,\n\
# I am 49 years old.\n\
# I love Rugby.'
# print(intro, '\n')
#
# intro = """Hello there!
# My name is Paata Mamporia,
# I am 49 years old.
# I love Rugby."""
# print(intro, '\n')
#
# intro = '''Hello there!
# My name is Paata Mamporia,
# I am 49 years old.
# I love Rugby.'''
# print(intro, '\n')
#
# intro = '''Hello there!
#             My name is Paata Mamporia,
#                             I am 49 years old.
#         I love Rugby.'''
# print(intro, '\n')


# ბრჭყალები ბრჭყალებში
# "Hello", said Susan!
# print("\"Hello\", said Susan!")
# print('"Hello", said Susan!')
# print("'Hello', said Susan!")
# print("""'Hello', said Susan!""")
# print(''''Hello', said Susan!''')
#
# # "Thet's my Teddy", said Pedro.
# print("\"Thet's my Teddy\", said Pedro.")
# print('"Thet\'s my Teddy", said Pedro.')
#
# print("c:\\ueser\\paata\\strings.py")
# print(r"c:\ueser\paata\strings.py")
# print(r"c:\ueser\paata\strings.py\n")


# ცარიელი სტრიქონი
# a = ''
# a = ""
# print(a)


# სტრიქონების შეკრება '+' ოპერატორით (კონკატენაცია)
# str1 = "Hello"
# str2 = "there"
# string = str1 + ' ' + str2 + "!"
# print(string)


# წვდომა სტრიქონის ელემენტებზე (სიმბოლოებზე)
# a = "Hello there!"
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[11], "\n")
#
# print(a[-1])
# print(a[-2])
# print(a[-3])


# ჭრები სტრიქონში Slice. სინტაქსი: string[start:stop:step]
# a = "Hello there!"
# print(a[0:4])           # პირველი ოთხი სიმბოლო
# print(a[:4])            # პირველი ოთხი სიმბოლო
# print(a[4:9])           # სიმბოლოები მითითებული დიაპაზონით
# print(a[2:9:3])         # სიმბოლოები მითითებული დიაპაზონით
# print(a[-4:])           # ბოლო ოთხი სიმბოლო
# print(a[3:])

# a = "Hello there!"
# print(a, id(a))
#
# a = 'P' + a[1:]
# print(a, id(a))
#
# a = 'H' + a[1:]
# print(a, id(a))
# print(a[1:], id(a[1:]))


# სტრიქონული მეთოდები

#1. სტრიქონის სიგრძე (სიმბოლოების რაოდენობა)  len()
# a = "Hello there!s"
# print(len(a))


#2. .capitalize(), .upper(), .lower(), .title()
# სინტაქსი: string.capitalize(), string.upper(), ...
# a = "i am hErE."
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.title())


#3. .count()
# სინტაქსი: string.count(word)
# a = '''Susan is a lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan...'''
# print(a.count('Susan'))
# print(a.count('Barky'))
# print(a.count('barky'))
# print(a.count('susan'))
# print(a.count('paata'))


#4. .strip(), .lstrip(), .rstrip()
# a = "      Hello there!   "
# a = a.strip()
# print(a)


#5. .replace(), .find(), .index()
# a = '''Susan is a lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan...'''
#
# a = a.replace('Susan', 'Ronny')
# print(a)

# a = 'I cyan love coding. I have fun with coding.'
# print(a.find('coding'))
# print(a.find('c'))
# print(a.find('Coding'), "\n")
#
# print(a.index('coding'))
# print(a.index('c'))
# print(a.index('Coding'), "\n")


#6. .split()
# სინტაქსი: string.split(separator, maxsplit)
# a = "I love coding."
# print(a.split())    # separator=' ' or separator='\n' or separator='\t', maxsplit=-1
#
# a = "I love coding.\nI have fun with\t\t\t\tcoding."
# print(a.split())    # separator=' ' or separator='\n' or separator='\t', maxsplit=-1
#
# a = "I love coding.\nI have fun with\t\t\t\tcoding."
# print(a.split('.'))    # separator=' ' or separator='\n' or separator='\t', maxsplit=-1
#
# a = "I love coding.\nI have fun with\t\t\t\tcoding."
# print(a.split('.\n'))    # separator=' ' or separator='\n' or separator='\t', maxsplit=-1

# a = "5+8=;15;18;13;14"
# print(a)
# print(a.split())
# print(a.split(';'))
# print(a.split(';')[3])


#7. .isalnum(), .isalpha(), .isnumeric()    <=====>  True / False   ჭეშმარიტი / მცდარი
# a = "numbers123numbers456"
# b = "numbers: 1235"
# print(a.isalnum())
# print(b.isalnum())

# a = "PaataMamporia"
# b = "Paata Mamporia"
# print(a.isalpha())
# print(b.isalpha())

# a = "125897136"   # a = int("12")      a = 12
# b = "25899.69"    # b = float("1.58")  b = 1.58
#                   # c = str(a + b)     c = "13.58"
# print(a.isnumeric())
# print(b.isnumeric())



#8. .islower(), .isupper(), .istitle()
# a = "paata mamporia"
# b = "paata mampOriA"
# print(a.islower())
# print(b.islower())

# a = "PAATA MAMPORIA"
# b = "paata mampOriA"
# print(a.isupper())
# print(b.isupper())

# a = "Paata Mamporia Is 49 Years Old."
# b = "Paata mamporia is 49 years old."
# print(a.istitle())
# print(b.istitle())



#9. სტრიქონის ფორმატირება
a = 14
b = 5.13
# Result: 4 + 5 = 9

print("Result:", a, "/", b, "=", a / b)
print("Result:", a, "/", b, "=", round(a / b, 2))
print("Result:", a, "/", b, "=", round(a / b, 3))
print("Result:", a, "/", b, "=", round(a / b, 0))

# f-სტრიქონი   f-string    f"lldfndlfn dslfnsd {a} / {b} = {a/b} kfjsnf lf"
print("Result: a / b = a / b")
print("Result: {a} / {b} = {a / b}")
print(f"Result: {a} / {b} = {a / b}")
print(f"Result: {a} / {b} = {round(a / b, 2)}")

result = f"Result: {a} / {b} = {round(a / b, 3)}"
print(result, type(result))

# a = 89
# b = 52
# print(result)


a = 14
b = 5.13
print(f"Result: {a} / {b} = {(a / b):.2f}")
print(f"Result: {a} / {b} = {(a / b):.3f}")
print(f"Result: {a} / {b} = {(a / b):10.3f}")
print(f"Result: {a} / {b} = {(a / b):<10.3f}")