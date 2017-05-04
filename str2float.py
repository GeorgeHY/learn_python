from functools import reduce
def  str2float(s):
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	def fn1(x,y):
		return x * 10 + y
	def fn2(x,y):
		return x / 10 + y
	m = s.split('.')
	u = list(map(char2num,m[0]))
	v = list(map(char2num,m[1]))
	q = v[::-1]

	return reduce(fn1,u)+reduce(fn2,q)/10