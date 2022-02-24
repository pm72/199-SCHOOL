# სტრიქონები  string

# a = "This is a string"
# print(a)
#
# a = 'This is a string'
# print(a)
#
# a = 'd'
# print(a, type(a))
#
# a = "12345"
# print(a, type(a))
#
# a = 12345
# print(a, type(a))


# მრავალსტრიქონიანი სტრიქონები
# intro = "Hello there! \
# My name is Paata mamporia, \
# I am 49 years old. \
# I love Rugby."
# print(intro)
#
# intro = "Hello there! " \
#         "My name is Paata mamporia, " \
#         "I am 49 years old. " \
#         "I love Rugby."
# print(intro)
#
# print()

# '\n'  ახალ სტრიქონზე გადასვლა   End line  New line   ENTER
# intro = "Hello there!\n\
# My name is Paata mamporia,\n\
# I am 49 years old.\n\
# I love Rugby."
# print(intro, "\n")
#
# intro = """Hello there!
# My name is Paata mamporia,
# I am 49 years old.
# I love Rugby."""
# print(intro, "\n")
#
# intro = '''Hello there!
# My name is Paata mamporia,
# I am 49 years old.
# I love Rugby.'''
# print(intro, "\n")
#
# intro = '''Hello there!
#             My name is Paata mamporia,
#                       I am 49 years old.
#         I love Rugby.'''
# print(intro, "\n")


# ბრჭყალები ბრჭყალებში
# "Hello", said Susan.
# print('"Hello", said Susan.')
# print("'Hello', said Susan.")
# print("""'Hello', said Susan.""")
#
# # "That's my Teddy", said Pedro.
# print("\"That's my Teddy\", said Pedro.")
# print('"That\'s my Teddy", said Pedro.')
# print(""""That's my Teddy", said Pedro.""")
#
# print("c:\\user\\paata\\strings.py")
# print(r"c:\user\paata\strings.py")
# print(r"c:\user\paata\strings.py\n")


# ცარიელი სტრიქონი
# a = ''
# a = ""
# print(a)


# სტრიქონების კონკატენაცია (შეწებება '+' ოპერატორით)
# str1 = "Hello"
# str2 = "there"
# string = str1 + " " + str2 + '!'
# print(string)
#
# # Suasan says "Hi"!
# a = 'Hi'
# print('Susan says "' + a + '"!')
# print('Daniel says "' + a + '"!')


# წვდომა სტრიქონის ელემენტებზე (სიმბოლოებზე)
# a = 'Hello there!'
# # print(a[0])
# # print(a[1])
# # print(a[2])
# # print(a[11], "\n")
# #
# # print(a[-1])
# # print(a[-2])
# # print(a[-3])


# ჭრები სტრიქონში Slice. სინტაქსი: string[start:stop:step]
# a = 'Hello there!'
# print(a[0:4])           # პირველი ოთხი სიმბოლო
# print(a[:4])            # პირველი ოთხი სიმბოლო
# print(a[2:7])           # სიმბოლოები მითითებული დიაპაზონით
# print(a[2:9:3])         # სიმბოლოები მითითებული დიაპაზონით
# print(a[-4:])           # ბოლო ოთხი სიმბოლო
# print(a[3:])


a = 'Hello there!'
print(a, id(a))

a = 'P' + a[1:]
print(a, id(a))

a = 'H' + a[1:]
print(a, id(a))