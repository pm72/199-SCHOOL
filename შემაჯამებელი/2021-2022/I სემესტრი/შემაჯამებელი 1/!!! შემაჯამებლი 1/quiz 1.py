def ex_1():
	print((9.5 * 4.5 - 2.5 * 3) / (45.5 - 3.5))


def ex_2():
	'''
	14 - 45.5    45 + 0.5 = 45.5   წთ
	x - 60

	x = 14 * 60 / 45.5   km   18.46??? km

	1 miles = 1 km * 1.6

	'''

	x = 14 * 60 / 45.5
	print(x / 1.6)


def ex_3():
	import random as r

	num = r.randint(100, 999)
	print(num)
	print(num // 60, num % 60)


def ex_4():
	a = 2.59
	b = -8.92
	d = (2 * b) / (a ** b)
	c = (a - 2 * b) / (d ** 2)
	r = (2.79 * a + 3 * d) / (b ** 2 - 2 * a * c)
	result = 4 / (3 * (r + 34)) - 9 * (a + b * c) + (3 + d * (2 + a)) / (a + b * d)

	print(result)


def ex_5():
	import math as m

	x1 = 1.5
	y1 = -3.4
	x2 = 4
	y2 = 5

	distance = m.sqrt(m.pow(x2 - x1, 2) + m.pow(y2 - y1, 2))
	print(((x1 - x2) ** 2 + (y2 - y1) ** 2) ** (1/2))
	print(distance)


def ex_6__7_class():
	x = 12.512 - 3.98j
	print((x.real + x.imag) / 2)


def ex_6__8_class():
	import random as r

	num = r.randint(1, 10 ** 12 - 1)
	print(num)

	max_ = min_ = num % 10
	num //= 10

	while num:   # whnum % 10ile num != 0   while num > 0
		dig = 
		if dig > max_:
			max_ = dig
		elif dig < min_:
			min_ = dig

		num //= 10

	print((max_ + min_) ** 2)


def ex_6__8_class__():
	import random as r

	num = r.randint(1, 10**12 - 1)
	print(num)

	max_ = min_ = num % 10
	num //= 10

	while num:
		digit = num % 10
		min_ = min(digit, min_)
		max_ = max(digit, max_)

		num //= 10

	print(min_, max_, (min_ + max_) ** 2)





# ===================
if __name__ == '__main__':
	# ex_1()
	# ex_2()
	# ex_3()
	# ex_4()
	# ex_5()
	# ex_6__7_class()
	# ex_6__8_class()
	# ex_6__8_class__()
	
	...
