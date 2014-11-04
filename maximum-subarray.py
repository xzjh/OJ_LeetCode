class Solution:
	# @param A, a list of integers
	# @return an integer
	def maxSubArray(self, A):
		if not A:
			return 0
		sums = 0
		max_sums = A[0]
		for i in range(len(A)):
			sums += A[i]
			max_sums = max(max_sums, sums)
			sums = max(sums, 0)
		return max_sums