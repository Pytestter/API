'''
Author：张来明
Date：2019-09-16
Describe：
'''

class Calculator():
	'''实现两个数的加减乘除'''
	def __init__(self,a,b):
		self.a = int(a)
		self.b = int(b)
	#加法
	def add(self):
		return self.a+self.b
	#减法
	def sub(self):
		return self.a-self.b
	#乘法
	def mul(self):
		return self.a * self.b
	#除法
	def div(self):
		return self.a / self.b
