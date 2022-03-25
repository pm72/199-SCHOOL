# სტრიქონები  string

# a = "This is a string"
# print(a)
#
# a = 'This is a string'
# print(a)
#
# a = "d"
# print(a, type(a))
#
# a = '12345'
# print(a, type(a))
#
# a = 123.45
# print(a, type(a))


# მრავალსტრიქონიანი სტრიქონები
# intro = "Hello there! \
# My name is Paata mamporia, \
# I am 19 years old. \
# I love Rugby."
# print(intro)
#
# intro = "Hello there! " \
#         "My name is Paata mamporia, " \
#         "I am 19 years old. " \
#         "I love Rugby."
# print(intro)
#
# print()

# '\n'  ახალ ხაზზე გადასვლა  New line  End line  ENTER
# intro = "Hello there!\n\
# My name is Paata mamporia,\n\
# I am 19 years old.\n\
# I love Rugby."
# print(intro, "\n")
#
# intro = """Hello there!
# My name is Paata mamporia,
# I am 19 years old.
# I love Rugby."""
# print(intro, "\n")
#
# intro = '''Hello there!
# My name is Paata mamporia,
# I am 19 years old.
# I love Rugby.'''
# print(intro, "\n")
#
# intro = '''Hello there!
#                 My name is Paata mamporia,
#                             I am 19 years old.
#         I love Rugby.'''
# print(intro, "\n")


# ბრწყალები ბრჭყალებში
# "Hello", said Susan.
# print(""Hello", said Susan.")
# print('"Hello", said Susan.')
# print("'Hello', said Susan.")
#
# # "That's is my Teddy", said Pedro.
# print("\"That's is my Teddy\", said Pedro.")
# print('"That\'s is my Teddy", said Pedro.')
# print(""""That's is my Teddy", said Pedro.""")
# print('''"That's is my Teddy", said Pedro.''')
#
# print("c:\\users\\paata\\strings.py")
# print(r"c:\users\paata\strings.py")
# print(r"c:\users\paata\strings.py\n")


# ცარიელი სტრიქონი
# a = ''
# a = ""
# print(a, type(a))


# ევდომა სტრიქონის სიმბოლოებზე
# a = "Hello there!"
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[11], "\n")
#
# print(a[-1])
# print(a[-2])
# print(a[-3])


# ჭრები სტრიქონში slice. სინტაქსი: string[start:stop-1:step=1]
# a = "Hello there!"
# print(a[0:4:1])         # პირველი ოთხი სიმბოლო
# print(a[0:4])           # პირველი ოთხი სიმბოლო
# print(a[:4])            # პირველი ოთხი სიმბოლო
# print(a[2:7])           # სიმბოლოები მითითებული დიაპაზონით
# print(a[2:9:3])         # სიმბოლოები მითითებული დიაპაზონით
# print(a[-4:])           # ბოლო ოთხი სიმბოლო
# print(a[3:])

# a = "Hello there!"
# print(a, id(a))
# # print(a[:-1] + " friends!")
#
# a = 'P' + a[1:]
# print(a, id(a))
#
# a = 'H' + a[1:]
# print(a, id(a))



# სტრიქონული მეთოდები

#1. სტრიქონის სიგრძე (სიმბოლოების რაოდენობა)  len()
# a = "Hello there!"
# print(len(a))
#
# a = "Hello       there!             "
# print(len(a))


#2. .capitalize(), .upper(), .lower(), .title()
# a = "i am hErE."
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.title())
# a = a.lower()
# print(a)


#3. .count()
# სინტაქსი: string.count(word)
# a = '''Susan is a lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan...'''
# print(a.count('Susan'))
# print(a.count('Barky'))
# print(a.count('barky'))
# print(a.count('Paata'))


#4. .strip(), .lstrip(), .rstrip()
# a = "          Hello there!   "
# print(a.strip())
#
# a = "*******numbers: 1234567890*******************"
# print(a.strip('*'))
# print(a.lstrip('*'))
# print(a.rstrip('*'))
#
# a = a.strip('*')
# print(a)


# 5. .replace(), .find(), .index()
# a = '''Susan is a lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan...'''
# a = a.replace('Susan', 'Ronny')
# print(a)

# a = "I cyan love coding. I have fun with coding."
# print(a.find('coding'))
# print(a.find('c'))
# print(a.find('Coding'))
#
# print()
#
# print(a.index('Coding'))
# print(a.index('coding'))
# print(a.index('c'))


#6. .split()
# სინტაქსი: string.split(separator, maxsplit)
# a = "I love coding."
# print(a.split())   # separator=' ' or separator='\n' or separator='\t', maxsplit=-1
#
# a = "I love coding.\nI have fun with\t\t\tcoding."
# print(a.split())   # separator=' ' or separator='\n' or separator='\t', maxsplit=-1
#
# a = "I love coding.\nI have fun with\t\t\tcoding."
# print(a.split('.'))   # separator=' ' or separator='\n' or separator='\t', maxsplit=-1
#
# a = "I love coding.\nI have fun with\t\t\tcoding."
# print(a.split('.\n'))   # separator=' ' or separator='\n' or separator='\t', maxsplit=-1

a = "2*3=;9;5;6;7"
print(a)
print(a.split(';'))
print(a.split(';')[3])