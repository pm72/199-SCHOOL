Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x, y = 45, 58
print(x, "+", y, "=", x+y)
45 + 58 = 103

print(f"{x} + {y} = {x + y}")
45 + 58 = 103


print(round(2/3, 2))
0.67
print(f"{2/3:.2f}{2/3:.2}")
0.670.67

print(f"{2/3:.2f} {2/3:.2e}")
0.67 6.67e-01
print(f"{5:.2f}")
5.00

print(f"{x}{y}")
4558
print(f"{x:10d}{y:10d}")
        45        58

print(f"{x:010d}{y:010d}")
00000000450000000058
print(f"{x:010d} {y:010d}")
0000000045 0000000058

print(f"{x:*>10d}{y:*>10d}")
********45********58

print(f"{x:<10d}{y:<10d}")
45        58        

print(f"{x:-<10d}{y:-<10d}")
45--------58--------

print(f"{x:<10d}{y:<10d}{2.5689156:<10.2f}")
45        58        2.57      

print(f"{x:<10d}{y:<10d}{2.5689156:<10.2f}{'Paata':<10s}")
45        58        2.57      Paata     

print(f"{x:<10d}{y:<10d}{'Paata':<4s}{2.5689156:<10.2f}")
45        58        Paata2.57      

print(f"{x:<10d}{y:<10d}{'Paata'}{2.5689156:<10.2f}")
45        58        Paata2.57      


print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}")
   Player              Country             Rating              Age

print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-'} * 69\n")
   Player              Country             Rating              Age
- * 69


print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}\n")
   Player              Country             Rating              Age
---------------------------------------------------------------------

>>> result = f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}\n"
>>> 
>>> print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------

>>> result = result + f"{' ':<3s}{'Jobava':<20s}{'Georgia':<20s}{2588:<20d}{38}\n{'-' * 69}\n"
>>> 
>>> print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------
   Jobava              Georgia             2588                38
---------------------------------------------------------------------

>>> result += f"{' ':<3s}{'Caruana':<20s}{'USA':<20s}{2781:<20d}{29}\n{'-' * 69}\n"
>>> print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------
   Jobava              Georgia             2588                38
---------------------------------------------------------------------
   Caruana             USA                 2781                29
---------------------------------------------------------------------

