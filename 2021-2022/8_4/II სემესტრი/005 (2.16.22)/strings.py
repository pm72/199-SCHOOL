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
a = 'Hello there!'
print(a[0:4])       # პირველი ოთხი სიმბოლო
print(a[:4])        # პირველი ოთხი სიმბოლო
print(a[5:9])       # სიმბოლეოები მოცემული დიაპაზონით
print(a[2:9:3])     # სიმბოლეოები მოცემული დიაპაზონით
print(a[-4:])       # ბოლოდან ოთხი სიმბოლო
print(a[3:])        # ბოლოდან ოთხი სიმბოლო