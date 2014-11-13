class MinStack:
	# @param x, an integer
	# @return an integer
	def __init__(self):
		self.stack = []
		self.min_stack = []
		
	def push(self, x):
		self.stack.append(x)
		if not self.min_stack or self.min_stack[-1] >= x:
			self.min_stack.append(x)

	# @return nothing
	def pop(self):
		if self.stack[-1] == self.min_stack[-1]:
			self.min_stack.pop()
		return self.stack.pop()

	# @return an integer
	def top(self):
		return self.stack[-1]

	# @return an integer
	def getMin(self):
		return self.min_stack[-1]
