class super:
	def hello(self):
		self.data1 = 'spam'
class sub(super):
	def hola(self):
		self.data2 = 'eggs'

if __name__=='__main__':
	X = sub()
	print(X.__dict__)
	print(X.__class__)
	print(sub.__bases__)
	print(super.__bases__)
	Y = sub()
	X.hello()
	print(X.__dict__)
	X.hola()
	print X.__dict__
	print sub.__dict__.keys()
	print super.__dict__.keys()
	print Y.__dict__