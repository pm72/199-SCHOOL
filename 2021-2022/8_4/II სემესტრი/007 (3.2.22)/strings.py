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
a = "Barky is Susan's best friend."
print('best friend' in a)
print('Best friend' in a)
