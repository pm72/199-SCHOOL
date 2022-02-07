# სტრიქონები   string

# a = 'This is a string'
# print(a)
#
# letter = 's'
# print(letter, type(letter))
#
# numbers = '123.56'
# print(numbers, type(numbers))
#
# numbers = 123.56
# print(numbers, type(numbers))


# მრავალსტრიქონიანი სტრიქონები
# intro = "Hello there! \
# My name is Paata Mamporia, \
# I love Rugby."
# print(intro)
#
# intro = "Hello there! " \
#         "My name is Paata Mamporia, " \
#         "I love Rugby."
# print(intro, "\n")
#
# intro = "Hello there!\n\
# My name is Paata Mamporia,\n\
# I love Rugby."
# print(intro, "\n")
#
# intro = """Hello there!
#     My name is Paata Mamporia,
#                   I love Rugby."""
# print(intro, "\n")
#
# intro = '''Hello there!
#     My name is Paata Mamporia,
#                   I love Rugby.'''
# print(intro, "\n")


# ბრწყალები ბრჭყალებში
# "Hello there!", said Susan
# print('"Hello there!", said Susan')
# print("'Hello there!', said Susan")
#
# print()
#
# # "That's my Teddy", said Pedro
# print("\"That's my Teddy\", said Pedro")
# print('"That\'s my Teddy", said Pedro')
# print('''"That's my Teddy", said Pedro''')
# print(""""That's my Teddy", said Pedro""")
# print(r"c:\user\paata\strings.py")
# print(r"c:\user\paata\strings.py\n")
# print("c:\\user\\paata\\strings.py\n")


# სტრიქონების კონკატენაცია
str1 = "Hello"
str2 = "there!"
string = str1 + " " + str2
print(string)

string = str2 + " " + str1
print(string)

print()

# Susan sais 'Hi!'
a = 'Hi!'
print("Susan sais '" + a + "'")