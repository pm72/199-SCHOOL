Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random

random_number = random.randint(100, 999)
wamebi = random_number%60
wutebi = (random_number - wamebi)/60
print(random_number)
print (int(wutebi), " ", wamebi)