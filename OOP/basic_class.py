class BasicClass:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart
	
	def addfunction(self):
		result = self.r + self.i
		return result

	
x = BasicClass(3.0, 4.5)
print(x.addfunction())
