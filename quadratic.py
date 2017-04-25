import math
def quadratic(a,b,c):
	if not isinstance(a, (int, float)):
		raise TypeError('bad operand type')
	if not isinstance(b, (int, float)):
		raise TypeError('bad operand type')
	if not isinstance(c, (int, float)):
		raise TypeError('bad operand type')
	d = b**2 - (4*a*c)
	if d < 0:
		print('无解')
	else:
		x1 = (-b + math.sqrt(d))/(2*a)
		x2 = (-b - math.sqrt(d))/(2*a)
		return x1, x2
	