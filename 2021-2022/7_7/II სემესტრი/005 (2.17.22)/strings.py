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

a = "Hello there!"
print(a, id(a))