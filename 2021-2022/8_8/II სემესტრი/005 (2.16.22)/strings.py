# სტრიქონები  string

# a = "This is a sring"
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
# a = 12345
# print(a, type(a))
#
# a = 12.345
# print(a, type(a))


# მრავალსტრიქონიანი სტრიქონები
# intro = "Hello there! \
# My name is paata Mamporia, \
# I am 49 years old. \
# I love Rugby."
# print(intro)
#
# intro = "Hello there! " \
#         "My name is paata Mamporia, " \
#         "I am 49 years old. " \
#         "I love Rugby."
# print(intro)
#
# print()
#
# # '\n'  ===>  ახალი სტრიქონი, New line, End line, ENTER
# intro = "Hello there!\n\
# My name is paata Mamporia,\n\
# I am 49 years old.\n\
# I love Rugby."
# print(intro, "\n")
#
# intro = """Hello there!
# My name is paata Mamporia,
# I am 49 years old.
# I love Rugby."""
# print(intro, '\n')
#
# intro = '''Hello there!
# My name is paata Mamporia,
# I am 49 years old.
# I love Rugby.'''
# print(intro, "\n")
#
# intro = '''Hello there!
#         My name is paata Mamporia,
#                   I am 49 years old.
#     I love Rugby.'''
# print(intro, "\n")


# ბრჭყლები ბრჭყალებში
# # "Hello", said Susan.
# print('"Hello", said Susan.')
# print("'Hello', said Susan.")
#
# print()
#
# # "That's my Teddy", said Pedro.
# print("\"That's my Teddy\", said Pedro.")
# print('"That\'s my Teddy", said Pedro.')
#
# print("c:\\user\\paata\\strings.py")
# print(r"c:\user\paata\strings.py")
# print(r"c:\user\paata\strings.py\n")


# სტრიქონების კონკატენაცია
str1 = "Hello"
str2 = "there!"
string = str1 + " " + str2
print(string)

string = str2 + " " + str1
print(string)

print()

# Susan sais "Hi"!
a = "Hi"
print('Susan sais "' + a + '"' + "!")
print('Susan sais "' + a + "\"!")