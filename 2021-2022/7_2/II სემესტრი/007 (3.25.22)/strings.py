# სტრიქონები   string

# a = "This is a string"
# print(a)
#
# a = 'This is a string'
# print(a)
#
# a = "s"
# print(a, type(a))
#
# a = '12345'
# print(a, type(a))
#
# a = 12.345
# print(a, type(a))


# მრავალსტრიქონიანი სტრიქონები
# intro = "Hello there! \
# My name is Paata Mamporia, \
# I am 49 yars old. \
# I love Rugby."
# print(intro)
#
# intro = "Hello there! " \
#         "My name is Paata Mamporia, " \
#         "I am 49 yars old. " \
#         "I love Rugby."
# print(intro)
#
# print()

# '\n'  ახალ ხაზზე გადასვლას  New line  End line  ENTER
# intro = "Hello there!\n\
# My name is Paata Mamporia,\n\
# I am 49 yars old.\n\
# I love Rugby."
# print(intro, "\n")
#
# intro = """Hello there!
# My name is Paata Mamporia,
# I am 49 yars old.
# I love Rugby."""
# print(intro, "\n")
#
# intro = '''Hello there!
# My name is Paata Mamporia,
# I am 49 yars old.
# I love Rugby.'''
# print(intro, "\n")
#
# intro = '''Hello there!
#             My name is Paata Mamporia,
#                       I am 49 yars old.
#       I love Rugby.'''
# print(intro, "\n")


# ბრწყალები ბრჭყალებში
# "Hello", said Susan.
# print('"Hello", said Susan.')
# print("'Hello', said Susan.")
# print("""'Hello', said Susan.""")
#
# # "That's is my Teddy", said Pedro.
# print("\"That's is my Teddy\", said Pedro.")
# print('"That\'s is my Teddy", said Pedro.')
# print('''"That's is my Teddy", said Pedro.''')
#
# a = '''"That's is my Teddy", said Pedro.'''
#
# print("c:\\user\\paata\\strings.py")
# print(r"c:\user\paata\strings.py")
# print(r"c:\user\paata\strings.py\n")


# ცარიელი სტრიქონი
# a = ""
# a = ''
# print(a, type(a))


# სტრიქონების „შეკრება“ '+' ოპერატორით (კონკატებაცია)
# str1 = "Hello"
# str2 = 'there'
# string = str1 + " " + str2 + "!"
# print(string)

# Susan sais "Hi"!
# a = 'Hi'
# print('susan sais "' + a + '"!')


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


# ჭრები სტრიქონში Slice. სინტქსი: string[start:stop:step]
# a = 'Hello there!'
# print(a[0:4:1])         # პირველი ოთხი სიმბოლო
# print(a[0:4])           # პირველი ოთხი სიმბოლო
# print(a[:4])            # პირველი ოთხი სიმბოლო
# print(a[2:9])           # სიმბოლოები მითითებული დიაპაზონით
# print(a[2:9:3])         # სიმბოლოები მითითებული დიაპაზონით
# print(a[-4:])           # ბოლო ოთხი სიმბოლო
# print(a[-4::2])
# print(a[::3])

# a = 'Hello there!'
# # print(a, id(a))
# #
# # a = 'p' + a[1:]
# # print(a, id(a))
# #
# # a = 'H' + a[1:]
# # print(a, id(a))


# სტრიქონული მეთოდები

#1. სტრიქონის სიგრძე (სიმბოლეობის რაოდენობა) len()
# a = "Hello there!"
# print(len(a))


#2. .capitalize(), .upper(), .lower(), .title()
# სინტაქსი: string.capitalize(), string.upper(), ...
# a = "i am hErE."
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.title())
#
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


#4. .strip(), .lstrip(), .rstrip()
# a = "           Hello world!  "
# print(a.strip())
#
# a = "********numbers: 12345*****************"
# print(a.strip('*'))
# print(a.lstrip('*'))
# print(a.rstrip('*'))
#
# a = a.strip('*')
# print(a)


#5. .replace(), .find(), .index()
# a = '''Susan is a lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan...'''
#
# a = a.replace('Susan', 'Ronny')
#
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


# 6. .split()
# სინტაქსი: string.split(separator, maxsplit)
a = "I love coding."
print(a.split())    # separator=' ' or separator='\n' or separator='\t', maxsplit=-1

a = "I love coding.\nI have fun with\t\t\tcoding."
print(a.split())    # separator=' ' or separator='\n' or separator='\t', maxsplit=-1

a = "I love coding.\nI have fun with\t\t\tcoding."
print(a.split('.'))    # separator=' ' or separator='\n' or separator='\t', maxsplit=-1

a = "I love coding.\nI have fun with\t\t\tcoding."
print(a.split('.\n'))    # separator=' ' or separator='\n' or separator='\t', maxsplit=-1