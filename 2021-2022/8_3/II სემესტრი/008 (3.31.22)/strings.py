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

#
# a = 'Hello there!'
# print(a, id(a))
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

#2. .capitalize(), .upper(), .lower(), .title()
# სინტაქსი: string.capitalize(), string.upper(), ...
# a = "i am hErE!"
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.title())

#3. count()
# სინტაქსი: string.count(word)
# a = '''Susan is a lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan...'''
# print(a.count('Susan'))
# print(a.count('Barky'))
# print(a.count('barky'))

#4. strip(), lstrip(), rstrip()
# a = "    Hello there!          "
# a = a.strip()
# print(a)
#
# a = "    Hello there!          "
# a = a.rstrip()
# print(a)
#
# a = "    Hello there!          "
# a = a.lstrip()
# print(a)

#5. .replace(), .find(), .index()
# a = '''Susan is a lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan...'''
#
# a = a.replace('Susan', 'Ronny')
#
# print(a)

# a = 'I cyan love coding. I have fun with coding.'
# print(a.find('coding'))
# print(a.find('c'))
# print(a.find('Coding'))
#
# print()
#
# print(a.index('coding'))
# print(a.index('c'))
# print(a.index('Coding'))

#6. .split()
# ინდექსი: string.split(separator, limit)
# a = "I love coding."
# print(a.split())   # separator=' ' or separator='\n' or separator='\t', limit=-1
#
# a = "I love coding.\nI have fun with\t\t\tcoding."
# print(a.split())   # separator=' ' or separator='\n' or separator='\t', limit=-1
#
# a = "I love coding.\nI have fun with\t\t\tcoding."
# print(a.split('.'))   # separator=' ' or separator='\n' or separator='\t', limit=-1
#
# a = "I love coding.\nI have fun with\t\t\tcoding."
# print(a.split('.\n'))   # separator=' ' or separator='\n' or separator='\t', limit=-1

# a = "6*5=;58;30;14;80"
# print(a)
# print(a.split(';'))
# print(a.split(';')[2])


#7. .isalnum(), .isalpha(), .isnumeric()   <======>  true / False   (ჭეშმარიტი / მცდარი)
# a = "numbers123numbers456"
# b = "numbers: 125899"
# print(a.isalnum())
# print(b.isalnum())

# a = "PaataMamporia"
# b = "Paata Mamporia"
# print(a.isalpha())
# print(b.isalpha())

# a = "1258976560"
# b = "158.69"
# print(a.isnumeric())
# print(b.isnumeric())



#8. .islower(), .isupper(), .istitle()
# a = 'paata mamporia is 49 years old'
# b = "Paata mamporia is 49 years old"
# print(a.islower())
# print(b.islower())

# a = 'paata mamporia is 49 years old'
# b = "PAATA MAMPORIA"
# print(a.isupper())
# print(b.isupper())

# a = 'Paata Mamporia Is 49 Years Old'
# b = "PAATA MAMPORIA"
# print(a.istitle())
# print(b.istitle())



#9. სტრიქონის ფორმატირება
a = 14
b = 5.13
# Result: 4 + 5 = 9

print("Result:", a, "/", b, "=", a / b)
print("Result:", a, "/", b, "=", round(a / b, 2))
print("Result:", a, "/", b, "=", round(a / b, 3))
print("Result:", a, "/", b, "=", round(a / b, 4))
print("Result:", a, "/", b, "=", round(a / b, 1))
print("Result:", a, "/", b, "=", round(a / b, 0))

# f-სტრიქონი  f-string    f"dm dlfnsldf {a} / {b} = {a / b}"
print("Result: a / b = a / b")
print("Result: {a} / {b} = {a} / {b}")
print(f"Result: {a} / {b} = {round(a / b, 2)}")

result = f"Result: {a} / {b} = {round(a / b, 2)}"
print(result)

print(f"Result: {a} / {b} = {(a / b):.2f}")
print(f"Result: {a} / {b} = {(a / b):.3f}")
print(f"Result: {a} / {b} = {(a / b):10.3f}")
print(f"Result: {a} / {b} = {(a / b):<10.3f}")