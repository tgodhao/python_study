X = 11

def f():
	print(X)
def g():
	X = 22
	print(X)
def g2():
	global X
	X = 22
def h1():
	X=33
	def nested():
		print(X)
# def h2():
# 	X=33
# 	def nested():
# 		nonlocal X
		# X = 44
class C:
	X = 33
	def m(self):
		X = 44
		self.X = 55
if __name__ == '__main__':
	print(X)
	f()
	g()
	print(X)
	obj=C()
	print(obj.X)
	obj.m()
	print(obj.X)
	print(C.X)
	print(X)
