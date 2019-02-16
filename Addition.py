class Addition:
	def __init__(self, first_digit, second_digit):
		self.first_digit = first_digit
		self.second_digit = second_digit
		print(str(first_digit)+" + "+str(second_digit)+" = ")
	def getResult(self):
		return self.first_digit+self.second_digit