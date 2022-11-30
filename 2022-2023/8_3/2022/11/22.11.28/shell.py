Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x, y = 45, 58    # 45 + 58 = 103
print(x, "+", y, "=", x + y)
45 + 58 = 103

print(x + y)
103

print(f"{x} + {y} = {
      }")
SyntaxError: unterminated string literal (detected at line 1)

print(f"{x} + {y} = {}")
SyntaxError: f-string: empty expression not allowed
print(f"{x} + {y} = {x + y}")
45 + 58 = 103


print(f"{x:.2f}")
45.00
print(f"{x:.f}")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(f"{x:.f}")
ValueError: Format specifier missing precision

print(f"{x:.1f}")
45.0

print(f"{x:.2f}")
45.00


print(f"{x}")
45
x = 45.269
print(f"{x}")
45.269




x = 2.589745
print(f"{x:.2f}")
2.59
y = 156
print(f"{x:.2f}{y}")
2.59156

print(f"{x:.2f} {y}")
2.59 156
print(f"{x:.2f}, {y}")
2.59, 156

print(f"{x:10.2f}, {y:10d}")
      2.59,        156

print(f"{x:10.2f}{y:10d}")
      2.59       156

print(f"{x:10.2f}{y:10}")
      2.59       156
print(f"{x:10.2}{y:10}")
       2.6       156

print(f"{x:010.2f}{y:010d}")
0000002.590000000156

print(f"{x:>10.2f}{y:>10d}")
      2.59       156
print(f"{x:->10.2f}{y:*>10d}")
------2.59*******156

print(f"{x:8>10.2f}{y:*>10d}")
8888882.59*******156


print(f"{x:<10.2f}{y:<10d}")
2.59      156       


print(f"{x:<3.2f}{y:<10d}")
2.59156       
2.59156
2.59156

print(f"{x:<.2f}{y:<10d}")
2.59156       

>>> 
>>> print(f"{x:<.0f}{y:<10d}")
3156       
>>> 
>>> 
>>> print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}")
   Player              Country             Rating              Age
>>> 
>>> print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}\n")
   Player              Country             Rating              Age
---------------------------------------------------------------------

>>> 
>>> 
>>> info = 
KeyboardInterrupt
f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}\n"
>>> 
>>> 
>>> info = f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}\n"
>>> 
>>> print(info)
   Player              Country             Rating              Age
---------------------------------------------------------------------

