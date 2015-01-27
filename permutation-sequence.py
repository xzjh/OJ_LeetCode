class Solution:
	# @return a string
	def getPermutation(self, n, k):
		
		def getFactorial(n):
			if n == 0:
				return 1
			return reduce(lambda x, y: x * y, range(1, n + 1))
		
		res = ''
		position = n - 1
		numberList = range(1, n + 1)
		while position >= 0:
			f = getFactorial(position)
			t = (k - 1) // f
			k %= f
			res += str(numberList[t])
			del numberList[t]
			position -= 1
		return res
