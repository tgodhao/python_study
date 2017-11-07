#coding:utf-8
class ShareData:
	'''
	类属性只能通过"类名.类属性"进行修改,实例只可引用.
	若强行赋值,则是在实例上创建一个与类属性同名的实例属性,

	'''
	data = 'spam'
	def __init__(self,value):
		#__init__构造方法,用于初始化实例属性. self.data 若没有进行赋值运算访问的是类属性,参与赋值运算,此时self.data是实例属性

		self.data = value
	def display(self):
		print(self.data,ShareData.data)

class NextClass:
	def printer(self,text):
		self.message = text
		print(self.message)

if __name__=='__main__':
	#测试类属性和实例属性的差异
	x = ShareData(1)
	y = ShareData(2)
	x.display();y.display()
	#方法的调用方式
	x = NextClass()
	x.printer('install call')
	x.message
	#类名调用
	NextClass.printer(x,'class call')


