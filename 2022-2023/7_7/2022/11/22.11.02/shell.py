Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math as m
m.sqrt(4)
2.0
4 ** 0.5
2.0

m.pi
3.141592653589793

m.sin(2 * m.pi)
-2.4492935982947064e-16
m.degrees(m.sin(2 * m.pi))
-1.4033418597069752e-14


help(min)
Help on built-in function min in module builtins:

min(...)
    min(iterable, *[, default=obj, key=func]) -> value
    min(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its smallest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the smallest argument.



help(m.pi)
Help on float object:

class float(object)
 |  float(x=0, /)
 |  
 |  Convert a string or number to a floating point number, if possible.
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __bool__(self, /)
 |      True if self else False
 |  
 |  __ceil__(self, /)
 |      Return the ceiling as an Integral.
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floor__(self, /)
 |      Return the floor as an Integral.
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(self, format_spec, /)
 |      Formats the float according to format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __round__(self, ndigits=None, /)
 |      Return the Integral closest to x, rounding half toward even.
 |      
 |      When an argument is passed, work like built-in round(x, ndigits).
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(self, /)
 |      Return the Integral closest to x between 0 and x.
 |  
 |  as_integer_ratio(self, /)
 |      Return integer ratio.
 |      
 |      Return a pair of integers, whose ratio is exactly equal to the original float
 |      and with a positive denominator.
 |      
 |      Raise OverflowError on infinities and a ValueError on NaNs.
 |      
 |      >>> (10.0).as_integer_ratio()
 |      (10, 1)
 |      >>> (0.0).as_integer_ratio()
 |      (0, 1)
 |      >>> (-.25).as_integer_ratio()
 |      (-1, 4)
 |  
 |  conjugate(self, /)
 |      Return self, the complex conjugate of any float.
 |  
 |  hex(self, /)
 |      Return a hexadecimal representation of a floating-point number.
 |      
 |      >>> (-0.1).hex()
 |      '-0x1.999999999999ap-4'
 |      >>> 3.14159.hex()
 |      '0x1.921f9f01b866ep+1'
 |  
 |  is_integer(self, /)
 |      Return True if the float is an integer.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __getformat__(typestr, /) from builtins.type
 |      You probably don't want to use this function.
 |      
 |        typestr
 |          Must be 'double' or 'float'.
 |      
 |      It exists mainly to be used in Python's test suite.
 |      
 |      This function returns whichever of 'unknown', 'IEEE, big-endian' or 'IEEE,
 |      little-endian' best describes the format of floating point numbers used by the
 |      C type named by typestr.
 |  
 |  __setformat__(typestr, fmt, /) from builtins.type
 |      You probably don't want to use this function.
 |      
 |        typestr
 |          Must be 'double' or 'float'.
 |        fmt
 |          Must be one of 'unknown', 'IEEE, big-endian' or 'IEEE, little-endian',
 |          and in addition can only be one of the latter two if it appears to
 |          match the underlying C reality.
 |      
 |      It exists mainly to be used in Python's test suite.
 |      
 |      Override the automatic determination of C-level floating point type.
 |      This affects how floats are converted to and from binary strings.
 |  
 |  fromhex(string, /) from builtins.type
 |      Create a floating-point number from a hexadecimal string.
 |      
 |      >>> float.fromhex('0x1.ffffp10')
 |      2047.984375
 |      >>> float.fromhex('-0x1p-1074')
 |      -5e-324
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  real
 |      the real part of a complex number



help(m.sin)
Help on built-in function sin in module math:

sin(x, /)
    Return the sine of x (measured in radians).



m.ceil(-2.5)
-2
m.ceil(2.5)
3

m.floor(-2.5)
-3
m.floor(2.5)
2

round(3.5)
4

round(5.5)
6

round(4.5)
4

round(2.5)
2

round(6.5)
6

round(1.5)
2
round(8.5)
8
round(8.50001)
9


round(-2.5)
-2


round(m.fabs(-2.5))
2

abs(1.58)
1.58

round(m.fabs(-13.5))
14

rad = m.radians(47)
rad
0.8203047484373349

deg = m.degrees(m.pi / 7)
deg
25.714285714285715


ch = 's'
ch
's'
type(ch)
<class 'str'>

text = "Welcome"
type(text)
<class 'str'>

text = 'Welcome'
type(text)
<class 'str'>


2**16
65536


'\u0065'
'e'
'\u0040'
'@'


print("Greck symbol ALPHA: \u03b1")
Greck symbol ALPHA: α
print("Greck symbol BETA: \u03b2")
Greck symbol BETA: β

print(f"\u03b1 = {m.degrees(m.pi / 2)}")
α = 90.0

m.pi / 2
1.5707963267948966


>>> print(f"\u03b1 = {m.degrees(m.pi)}")
α = 180.0
>>> 
>>> 
>>> '\u10d0'
'ა'
>>> '\u10d1'
'ბ'
>>> '\u10d2'
'გ'
>>> 
>>> 
>>> 'a'
'a'
>>> \
... 
... 
... as
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 'თ'
'თ'
>>> 
>>> 
>>> print("Goto 🅆")
Goto 🅆
