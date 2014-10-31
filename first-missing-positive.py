class Solution:
	# @param A, a list of integers
	# @return an integer
	def firstMissingPositive(self, A):
		length = len(A)
		if not A:
			return 1
		for i in range(length):
			while A[i] != i + 1 and A[i] >= 1 and A[i] <= length and A[i] != A[A[i] - 1]:
				s = A[i] - 1
				A[i], A[s] = A[s], A[i]
		for i in range(length):
			if A[i] != i + 1:
				return i + 1
		return length + 1

s = Solution()
print s.firstMissingPositive([2,1])