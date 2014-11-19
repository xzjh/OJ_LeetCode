class Solution:
	# @return a list of integers
	def grayCode(self, n):
		
		res = [0] * (2 ** n)
		
		for i in range(n):
			for j in range(2 ** i, 2 ** (i + 1)):
				res[j] = res[j - 2 * (j - 2 ** i) - 1] + 2 ** i
		return res
