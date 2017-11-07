#coding:utf-8
from classtools import AttrDisplay
class Person(AttrDisplay):
	def __init__(self,name,job=None,pay=0):
		self.name = name
		self.job = job
		self.pay = pay
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self,percent):
		self.pay = int(self.pay * (1+percent))
	
class Manager(Person):
	def __init__(self,name,pay):
		Person.__init__(self,name,'mgr',pay)
	def giveRaise(self,percent,bonus=.10):
		#这种方式不好,不利于维护
		#self.pay = int(self.pay * (1+percent+bonus))
		Person.giveRaise(self,percent+bonus)
#组合实现Manager
# class Manager:
# 	def __init__(self,name,pay):
# 		self.person = Person(name,'mgr',pay)
# 	def giveRaise(self,percent,bonus=.10):
# 		self.person.giveRaise(percent+bonus)
# 	def __getattr__(self,attr):
# 		return getattr(self.person,attr)
# 	def __str__(self):
# 		return str(self.person)
		
if __name__ == '__main__':

	
	bob = Person('Bob Smith')
	sue = Person('Sue Jones',job='dev',pay=100000)
	print(bob)
	print(sue)
	#print ('{0} {1}' .format(bob.name,bob.pay))
	print(bob.lastName(),sue.lastName())
	sue.giveRaise(.10)
	print(sue.pay)
	print(sue)
	tom = Manager('Tom Jones',50000)
	tom.giveRaise(.10)
	print(tom.lastName())
	print(tom.job)
	print(tom)
	print('--All three--')
	for object in (bob,sue,tom):
		object.giveRaise(.10)
		print(object)
	#组合测试
	# bob = Person('hao shen','test',50000)
	# sue = Person('god hao','doctor',5000)
	# tom = Manager('deng hao',90000)
	# class Department:
	# 	def __init__(self,*args):
	# 		self.members = list(args)
	# 	def addMember(self,person):
	# 		self.members.append(person)
	# 	def giveRaise(self,percent):
	# 		for person in self.members:
	# 			person.giveRaise(percent)
	# 	def showAll(self):
	# 		for person in self.members:
	# 			print(person)
	# development = Department(bob,sue)
	# development.addMember(tom)
	# development.giveRaise(.10)
	# development.showAll()
			
