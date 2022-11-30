Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math as m
r = 3.895478
length = 2 * m.pi * r
area = m.pi * r ** 2

print("The length is", round(length, 2), "and the area is", round(area, 2))
The length is 24.48 and the area is 47.67

print(f"The length is {length} and the area is {area}")
The length is 24.47601013404132 and the area is 47.67287950246752

print(f"The length is {length:.2f} and the area is {area:.2}")
The length is 24.48 and the area is 4.8e+01
print(f"The length is {length:.2f} and the area is {area:.2f}")
The length is 24.48 and the area is 47.67


x, y = 45, 58
print(f"{x:.2f} {y:.2f}")
45.00 58.00

print(f"{x}{y}")
4558
print(f"{x:10d}{y:10d}")
        45        58

print(f"{x:010d}{y:010d}")
00000000450000000058
print(f"{x:<10d}{y:<10d}")
45        58        

print(f"{x:<10d}{y:<10d}{2.589254:<10.2f}")
45        58        2.59      

print(f"{x:<10d}{y:<10d}{2.589254:<10.2f}{'Paata':<10s}")
45        58        2.59      Paata     

print(f"{x:<10d}{y:<10d}{2.589254:<10.2f}{'Paata'}")
45        58        2.59      Paata

print(f"{x:<10d}{y:<10d}{2.589254:<10.2f}Paata")
45        58        2.59      Paata

print(f"{x:<10d}{y:<10d}{2.589254:<10.2f}{'Paata'}")
45        58        2.59      Paata

print(f"{x:<10d}{y:<10d}{2.589254:<3.2f}{'Paata'}")
45        58        2.59Paata

print(f"{x:<10d}{y:<10d}{2.589254:<10.2f}{'Paata'}")
45        58        2.59      Paata

print(f"{x:<10d}{y:<10d}{'Paata'}{2.589254:<10.2f}")
45        58        Paata2.59      


print(f"{' ':<3s}{'Player'}{'Country'}'Rating:.2f'")
   PlayerCountry'Rating:.2f'

print(f"{' ':<3s}{'Player':<10s}{'Country':<10s}{'Rating':<10s}{'Age'}")
   Player    Country   Rating    Age

print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}")
   Player              Country             Rating              Age

print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}")
   Player              Country             Rating              Age
---------------------------------------------------------------------


result = f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n"

print(result)
   Player              Country             Rating              Age

>>> 
>>> result = f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}\n"
>>> 
>>> print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------

>>> result +=  f"{' ':<3s}{'Jobava':<20s}{'Georgia':<20s}{2588:<20d}{38}\n{'-' * 69}\n"
>>> 
>>> print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------
   Jobava              Georgia             2588                38
---------------------------------------------------------------------

>>> result = result +  f"{' ':<3s}{'Caruana':<20s}{'USA':<20s}{2781:<20d}{29}\n{'-' * 69}\n"
>>> 
>>> print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------
   Jobava              Georgia             2588                38
---------------------------------------------------------------------
   Caruana             USA                 2781                29
---------------------------------------------------------------------

