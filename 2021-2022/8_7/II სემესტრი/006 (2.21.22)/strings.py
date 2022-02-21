# სტრიქონი  string

# a = "This is a string"
# print(a)
#
# a = 'This is a string'
# print(a)
#
# b = "d"
# print(b, type(b))
#
# numbers = '1234'
# print(numbers, type(numbers))


# მრავალსტრიქონიანი სტრიქონი
# intro = "Hello there! \
# My name is Paata Mamporia, \
# I love Rugby!"
#
# print(intro, "\n")     # \n  -   ENTER
#
# intro = "Hello there!\n\
# My name is Paata Mamporia,\n\
# I love Rugby!"
#
# print(intro, "\n")
#
# intro = "Hello there" \
#         "My name is Paata Mamporia" \
#         "I love Rugby"
# print(intro, "\n")
#
# intro = """Hello there!
# My name is Paata Mamporia,
# I love Rugby!"""
# print(intro, "\n")
#
# intro = \
# '''Hello there!
#     My name is Paata Mamporia,
#         I love Rugby!'''
# print(intro)


# ბრჭყალები სტრიქონში
# # "Hello there", said Susan
# print('"Hello there", said Susan')
# print("'Hello there', said Susan")
#
# print()
#
# # "That's my Taddy", said Pedro
# print("\"That's my Taddy\", said Pedro")
# print('"That\'s my Taddy", said Pedro')
# print(""""That's my Taddy", said Pedro""")
# print('''"That's my Taddy", said Pedro''')
# print("c:\\user\\paata\\strings.py")
# print(r"c:\user\paata\strings.py")
# print(r"c:\user\paata\strings.py\n")
# print("c:\\user\\paata\\strings.py\n")


# სტრიქონების კონკატენაცია
# str1 = "Hello"
# str2 = "there!"
# string = str1 + " " + str2
# print(string)
#
# print()
#
# # Susan sais 'Hi'
# a = 'Hi'
# print("Susan sais '" + a + "'")


# ცარიელი სტრიქონი
# a = ''
# a = ""
# print(a)


# წვდომა სტრიქონის სიმბოლოებთან
# a = "Hello there!"
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[11])
# print(a[-1])
# print(a[-2])
# print(a[-3])


# ჭრები სტრიქონში  slice
# a = "Hello there!"
#
# print(a[0:4])     # პირველი ოთხი სომბოლო
# print(a[:4])      # პირველი ოთხი სომბოლო
# print(a[7:12])    # სიმბოლოები მოცემული დიაპაზონით
# print(a[-4:])     # ბოლო ოთხი სომბოლო
#
# print()
# print(a)

# a = "Hello there!"
# print(a, id(a))
#
# a = a[:6] + 'friends!'
# print(a, id(a))
#
# a = 't' + a[1:]
# print(a, id(a))


# სტრიქონული მეთოდები
# სტრიქონის სიგრძე  len()    len(string)
# a = "Hello there!"
# print(len(a))


# .capitalize(), .upper(), .lower(), .title()
# a = "i am here!"
# print(a.capitalize())
# print(a.upper())
#
# a = "I AM Here!"
# print(a.lower())
#
# a = "i love rugby!"
# print(a.title())
# print(a)


#1. .count()
# სინტქასი: string.count(word)
# a = '''Susan is a lovely girl.
# Burky is Susan's friend.
# Burky plays with Susan.'''
# print(a.count('Susan'))
# print(a.count('Burky'))
# print(a.count('burky'))
# print(a.count('susan'))

#2. strip(),  .rstrip(), .lstrip()
# a = "     I love coding.    "
# print(a)
# print(a.strip())

#3. .replace(), .find(), .index()
# a = '''Susan is a lovely girl.
# Burky is Susan's friend.
# Burky plays with Susan.'''
# print(a.replace('Susan', 'Ronny'))

# a = 'I love coding. I have fun with coding.'
# print(a.find('coding'))
# print(a.find('Coding'))
# print(a.index('coding'))
# # print(a.index('Coding'))
# print(a.index('c'))

#4. .split()
# სინტაქსი: string.split(separator, limit)
# a = 'I love coding.'
# print(a.split())    # separator=' ', separator='\t', separator='\n',

a = 'I love coding.\nI have fun\t\twith coding!'
# print(a)
# print(a.split())    # separator=' ', separator='\t', separator='\n',

a = 'I love coding.\nI have fun\t\twith coding!'
# print(a)
# print(a.split('.\n'))    # separator=' ', separator='\t', separator='\n',

# a = "2+3= 8 9 6 5"
# a = a.split()
# print(a)
# print(a[0])
# print(eval(a[0][:-1]))
# print(eval('1.1 == 3.3'))

# ოპერატორი 'in'
print('coding' in 'A love coding.')
print('Coding' in 'A love coding.')