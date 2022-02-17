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

a = "Hello there!"
print(a, id(a))

a = 'P' + a[1:]
print(a, id(a))

a = 'H' + a[1:]
print(a, id(a))
print(a[1:], id(a[1:]))
