# -*- coding: utf-8 -*-

class ExClass:
	def __init__(self, val1, val2):
		self.val1 = val1
		self.val2 = val2

if __name__ == '__main__':
	example = ExClass(10 , 20)
	print("val1 = " + str(example.val1))
	print("val2 = " + str(example.val2))
		