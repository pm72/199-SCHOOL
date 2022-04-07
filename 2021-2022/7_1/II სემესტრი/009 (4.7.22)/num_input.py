# x = input("Number one: ")         # input() ფუნქცია აბრუნებს სტრიქონს  type str
# y = input("Number two: ")
# add = x + y
#
# print(f"The sum is {x} + {y} = {add}")
# print(type(x), type(y), type(add))

# x = int(input("Number one: "))
# y = int(input("Number two: "))
# add = x + y
#
# print(f"The sum is {x} + {y} = {add}")
# print(type(x), type(y), type(add))

# x = float(input("Number one: "))
# y = float(input("Number two: "))
# add = x + y
#
# print(f"The sum is {x} + {y} = {add}")
# print(type(x), type(y), type(add))

# x = eval(input("Number one: "))
# y = eval(input("Number two: "))
# add = x + y
#
# print(f"The sum is {x} + {y} = {add}")
# print(type(x), type(y), type(add))

print(eval("5 * 9"))
print(eval("5 * (9 + 2.56) ** (1.24 / 3.91)"))
print(5 * (9 + 2.56) ** (1.24 / 3.91))
print("Welcome " + eval("input('Your name: ')") + "!")