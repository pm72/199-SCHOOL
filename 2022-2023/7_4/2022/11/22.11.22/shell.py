Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math as m
r = 3.8956474
length = 2 * m.pi * r
area = m.pi * r ** 2

print("The length is", round(length, 2), "and the area is", round(area, 2))
The length is 24.48 and the area is 47.68

print(f"The length is {length} and the area is {area}")
The length is 24.477074505632356 and the area is 47.67702582873649

print(f"The length is {length:.2f} and the area is {area:.2}")
The length is 24.48 and the area is 4.8e+01
print(f"The length is {length:.2f} and the area is {area:.2f}")
The length is 24.48 and the area is 47.68


x, y = 45, 58
print(f"{x} + {y} = {x + y}")    # 45 + 58 = 103
45 + 58 = 103


print(f"x = {x:.2f}")       # 45.00
x = 45.00

print('-'* 100)
----------------------------------------------------------------------------------------------------

print(f"{x:10d}{y:10d}")
        45        58
print(f"{x:<10d}{y:<10d}")
45        58        

print(f"{x:<10d}{y:<10d}{2.56894:<10.2f}")
45        58        2.57      

print(f"{x:<10d}{y:<10d}{2.56894:<10.2f}{'Paata':<10s}")
45        58        2.57      Paata     
print(f"{x:<10d}{y:<10d}{2.56894:<10.2f}{'Paata'}")
45        58        2.57      Paata
print(f"{x:<10d}{y:<10d}{2.56894:<10.2f}Paata")
45        58        2.57      Paata

print(f"{x:<10d}{y:<10d}{2.56894:<-10.2f}{Paata}")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(f"{x:<10d}{y:<10d}{2.56894:<-10.2f}{Paata}")
NameError: name 'Paata' is not defined

print(f"{x:<10d}{y:<10d}{2.56894:<'*'10.2f}{Paata}")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(f"{x:<10d}{y:<10d}{2.56894:<'*'10.2f}{Paata}")
ValueError: Invalid format specifier
print(f"{x:<10d}{y:<10d}{2.56894:<010.2f}{Paata}")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(f"{x:<10d}{y:<10d}{2.56894:<010.2f}{Paata}")
NameError: name 'Paata' is not defined
print(f"{x:<10d}{y:<10d}{2.56894:<010.2f}{'Paata'}")
45        58        2.57000000Paata
print(f"{x:<10d}{y:<10d}{2.56894:<-10.2f}{'Paata'}")
45        58        2.57      Paata
print(f"{x:<10d}{y:<10d}{2.56894:<*10.2f}{'Paata'}")
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(f"{x:<10d}{y:<10d}{2.56894:<*10.2f}{'Paata'}")
ValueError: Invalid format specifier
print(f"{x:<10d}{y:<10d}{2.56894:<'*'10.2f}{'Paata'}")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(f"{x:<10d}{y:<10d}{2.56894:<'*'10.2f}{'Paata'}")
ValueError: Invalid format specifier
print(f"{x:<10d}{y:<10d}{2.56894:-<10.2f}{'Paata'}")
45        58        2.57------Paata
print(f"{x:<10d}{y:<10d}{2.56894:*<10.2f}{'Paata'}")
45        58        2.57******Paata
print(f"{x:*<10d}{y:-<10d}{2.56894:*<10.2f}{'Paata'}")
45********58--------2.57******Paata
print(f"{x:<10d}{y:<10d}{2.56894:<10.2f}{'Paata'}")
45        58        2.57      Paata


print(f"{' ':<3s}{'Player:<20s'}{'Country':<20s}{'Rating':<20s}{'Age'}")
   Player:<20sCountry             Rating              Age

print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}")
   Player              Country             Rating              Age


print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}")
   Player              Country             Rating              Age
---------------------------------------------------------------------


result = f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}\n"

print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------

>>> 
>>> res
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    res
NameError: name 'res' is not defined
>>> 
>>> result = result + f"{' ':<3s}{'Jobava':<20s}{'Georgia':<20s}{2588:<20d}{38}\n{'-' * 69}\n"
>>> 
>>> print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------
   Jobava              Georgia             2588                38
---------------------------------------------------------------------

>>> result += f"{' ':<3s}{'Caruana':<20s}{'USA':<20s}{2781:<20d}{29}\n{'-' * 69}\n"
>>> 
>>> print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------
   Jobava              Georgia             2588                38
---------------------------------------------------------------------
   Caruana             USA                 2781                29
---------------------------------------------------------------------

