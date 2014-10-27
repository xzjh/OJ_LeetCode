class Solution:
	# @param A, a list of integer
	# @return an integer
	def singleNumber(self, A):
		ones = 0
		twos = 0
		for i in range(len(A)):
			twos |= ones & A[i]
			ones ^= A[i]
			threes = ones & twos
			ones &= ~threes
			twos &= ~threes
		return ones
		