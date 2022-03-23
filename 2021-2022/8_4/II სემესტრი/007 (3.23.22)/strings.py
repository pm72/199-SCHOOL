# სტრიქონი   string

# a = "This is a string"
# print(a)
#
# a = 'This is a string'
# print(a)
#
# a = '123568'
# print(a, type(a))
#
# a = 123568
# print(a, type(a))
#
# a = 123.568
# print(a, type(a))


# მრავალსტრიქონიანი სტრიქონები
# intro = "Hello there! \
# My name is Paata mamporia, \
# I am 49 years old. \
# I love Rugby."
# print(intro)
#
# intro = 'Hello there! ' \
#         'My name is Paata mamporia, ' \
#         'I am 49 years old. ' \
#         'I love Rugby.'
# print(intro)
#
# print()
#
# # '\n' ====> ახალ ხაზზე გადასვლას  New Line, End line, ENTER
# intro = 'Hello there!\n' \
#         'My name is Paata mamporia,\n' \
#         'I am 49 years old.\n' \
#         'I love Rugby.'
# print(intro, "\n")
#
# intro = """Hello there!
# My name is Paata mamporia,
# I am 49 years old.
# I love Rugby."""
# print(intro, '\n')
#
# intro = '''Hello there!
# My name is Paata mamporia,
# I am 49 years old.
# I love Rugby.'''
# print(intro, "\n")
#
# intro = '''Hello there!
#       My name is Paata mamporia,
#                   I am 49 years old.
#   I love Rugby.'''
# print(intro, "\n")


# ბრჭყალები ბრჭყალებში
# # "Hello", said Susan.
# print("\"Hello\", said Susan.")
# print('"Hello", said Susan.')
# print("'Hello', said Susan.")
#
# print()
#
# # "That's is my Teddy", said Pedro.
# print("\"That's is my Teddy\", said Pedro.")
# print('"That\'s is my Teddy", said Pedro.')
#
# print("c:\\user\\paata\\strings.py")
# print(r"c:\user\paata\strings.py")
# print(r"c:\user\paata\strings.py\n")


# სტრიქონების კონკატენაცია
# str1 = "Hello"
# str2 = "there!"
# string = str1 + " " + str2
# print(string)
#
# string = str2 + " " + str1
# print(string)


# ინდექსაცია სტრიქონებში
# a = 'Hello there!'
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[11], "\n")
#
# print(a[-1])
# print(a[-2])
# print(a[-3])
# print(a[-4])


# ჭრები სტრიქონში Slice. სინტაქსი string[start:stop:step]
# a = 'Hello there!'
# print(a[0:4])       # პირველი ოთხი სიმბოლო
# print(a[:4])        # პირველი ოთხი სიმბოლო
# print(a[5:9])       # სიმბოლეოები მოცემული დიაპაზონით
# print(a[2:9:3])     # სიმბოლეოები მოცემული დიაპაზონით
# print(a[-4:])       # ბოლოდან ოთხი სიმბოლო
# print(a[3:])        # ბოლოდან ოთხი სიმბოლო


# სტრიქონული მეთოდები

#1. len()  სტრიქონის სიგრძე (სიმბოლოების რაოდენობა)
# a = "Hello there!"
# print(len(a))


#2. .capitalize(), .upper(), .lower(), .title()
# სინტაქსი: string.capitalize(), string.upper()
# a = "hello there!"
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.title())


#3. .count()
# სინტაქსი: string.count(word)
# a = '''Susan is a lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan.'''
# print(a.count('Susan'))
# print(a.count('Barky'))
# print(a.count('barky'))


#4. .strip(), .lstrip(), .rstrip()
# a = '          Hello there!    '
# a = a.strip()
# print(a)


#5. .replace(), .find(), .index()
# a = '''Susan is a lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan.'''
#
# a = a.replace('Susan', 'Ronny')
# print(a)

# a = "I cyan love coding. I have fun with Python coding."
# print(a.find('coding'))
# print(a.find('c'))
# print(a.find('Coding'))
#
# print(a.index('coding'))
# print(a.index('Coding'))


#6. .split()
# სინტაქსი: string.split(separator, limit)
# a = "I love coding."
# print(a.split())   # separator=' ' and separator='\n' and separator='\t', limit=inf
#
# a = "I love coding.\nI have fun with Pyrhon coding."
# print(a.split('.'))   # separator=' ' and separator='\n' and separator='\t', limit=inf
#
# a = "I love coding.\nI have fun with Pyrhon coding."
# print(a.split('.\n'))   # separator=' ' and separator='\n' and separator='\t', limit=inf
#
# a = "numbers#123#numbers#456#numbers#789"
# print(a.split('#'))   # separator=' ' and separator='\n' and separator='\t', limit=inf
# print(a.split('#', 1))   # separator=' ' and separator='\n' and separator='\t', limit=inf
# print(a.split('#', 2))   # separator=' ' and separator='\n' and separator='\t', limit=inf
# print(a.split('#', 3))   # separator=' ' and separator='\n' and separator='\t', limit=inf


#7. ოპერატორი 'in'  ====> True / False  (ჭეშმარიტი / მცდარი)
# a = "Barky is Susan's best friend."
# print('best friend' in a)   # True
# print('Best friend' in a)   # False


#8. .isalnum(), .isalpha(), .isnumeric()
# a = "numbers123number456"
# b = "numbers 123 number456"
# print(a.isalnum())
# print(b.isalnum())

# a = "PaataMamporia"
# b = "Paata Mamporia"
# print(a.isalpha())
# print(b.isalpha())

# a = "1235897120355"
# b = "1259.69"
# print(a.isnumeric())
# print(b.isnumeric())


#9. .islower(), .isupper(), .istitle()
# a = "paata mamporia ---> 49 old."
# b = "Paata mamporia ---> 49 old."
# print(a.islower())
# print(b.islower())

# a = "PAATA MAMPORIA ---> 49 OLD."
# b = "Paata mamporia ---> 49 old."
# print(a.isupper())
# print(b.isupper())

# a = "Paata Mamporia ---> 49 Old."
# b = "Paata mamporia ---> 49 old."
# print(a.istitle())
# print(b.istitle())


#10. სტრიქონების ფორმატირება
# a = 14
# b = 51.12
# # Result: 4 + 5 = 9
#
# print("Result:", a, "/", b, "=", a / b)
# print("Result:", a, "/", b, "=", round(a / b, 2))
# print("Result:", a, "/", b, "=", round(a / b, 3))
#
# # f-სტრიქონი  f-string   f"{} {} {}"
# print("Result: a / b = a/b")
# print("Result: {a} / {b} = {a/b}")
# print(f"Result: {a} / {b} = {a/b}")
# print(f"Result: {a} / {b} = {round(a/b, 2)}")
# print(f"Result: {a} / {b} = {(a / b):.2f}")
# print(f"Result: {a} / {b} = {(a / b):.3f}")
# print(f"Result: {a} / {b} = {(a / b):.1f}")
# print(f"Result: {a} / {b} = {(a / b):.0f}")
#
# # შაბლონები, ესკიზები, Templates
# # "{} {} ... {}".format(arg1, arg2, ..., argN)
# print("Result: {} / {} = {}".format(a, b, a/b))
# print("Result: {} / {} = {:.2f}".format(a, b, a/b))

result = "{} / {} = {:.2f} {}"

a = 14
b = 51
# print(result.format(a, b, a/b))
print(result.format(a, b, a / b, a + b))