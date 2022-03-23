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

# a = "I love coding. I have fun with Python coding."
# print(a.find('coding'))
# print(a.find('c'))
#
# ind = a.find('coding')
# print(a[ind:ind+len('coding')])
# print(a.find('Coding'))

# print(a.index('coding'))
# print(a.index('Coding'))


# ინდექსები სტრიქონში    string[index]
# a = "Hello there!"
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[len(a)-1], "\n")
#
# print(a[-1])
# print(a[-2])
# print(a[-3])


# ჭრები სტრიქონში  slice.       string[start:stop:step]   <===>  string[start=0:stop-1:step=1]
# a = "Hello there!"
# print(a[0:3:1])       # პირველი სამი სიმბოლო
# print(a[0:3])         # პირველი სამი სიმბოლო
# print(a[:3])          # პირველი სამი სიმბოლო
# print(a[2:7])         # სიმბოლოები მითითებული დიაპაზონით
# print(a[2:9:3])       # სიმბოლოები მითითებული დიაპაზონით
# print(a[:7:2])
# print(a[4:])
# print(a[-4:])
# print(a[-4::2])
# print(a[2:-4])

# a = "hello there!"
# # a[0] = 'H'
# print(a, id(a))
# a = 'H' + a[1:]
# print(a, id(a))


# ოპერატორი in    True / False  (ჭეშმარიტი / მცდარი)
# a = "Paata is Demetre's father."
# print("Demetre" in a)
# print("demetre" in a)
# print("Paata" in a)
# print("paata" in a)
# print("u" in a)


# .isalnum(), .isalpha(), isnumeric()
# a = "numbers123numbers456"
# b = "numbers 123"
# print(a.isalnum())
# print(b.isalnum())

# a = "PaataMamporia"
# b = "Paata Mamporia"
# print(a.isalpha())
# print(b.isalpha())

# a = "123458970145"
# b = "2589.36"
# print(a.isnumeric())
# print(b.isnumeric())


# .islower(), .isupper(), .istitle()
# a = "paata mamporia ---> 49 old."
# b = "Paata mamporia ---> 49 old."
# print(a.islower())
# print(b.islower())

# a = "PAATA ---> 49 OLD."
# b = "Paata ---> 49 old."
# print(a.isupper())
# print(b.isupper())

# a = "Paata Mamporia ---> 49 Old."
# b = "Paata ---> 49 old."
# print(a.istitle())
# print(b.istitle())


# სტრიქონის ფორმატირება
# a = 14
# b = 5.36
#
# # Result: 4 + 5 = 9
#
# print("Result:", a, "/", b, "=", a / b)
# print("Result:", a, "/", b, "=", round(a / b, 2))
#
# # f-სტრიქონი  f-string
# print("Result: a / b = a/b")
# print("Result: {a} / {b} = {a/b}")
# print(f"Result: {a} / {b} = {a/b}")
# print(f"Result: {a} / {b} = {round(a/b, 2)}")
# print(f"Result: {a} / {b} = {round(a/b, 3)}")
# print(f"Result: {a} / {b} = {(a/b):.3f}")
#
# # ფორმატირება    "{} {} ... {}".format(arg1, arg2, ..., argN)
# print("Result: {} / {} = {:.2f}".format(a, b, a/b))

# შაბლონები,  ესკიზები
result = "Result: {} / {} = {}"

a = 14
b = 19
print(result.format(a ,b, a/b))

# --========-----

x = 1.4
y = -2.98
print(result.format(x ,y, x/y))