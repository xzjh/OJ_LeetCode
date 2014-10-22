class Solution:
	# @param a list of integers
	# @return an integer
	def removeDuplicates(self, A):
		length = len(A)
		if length <= 1:
			return length
		i = 0
		j = 1
		while j < length:
			while j < length and A[i] == A[j]:
				j += 1
			if j >= length:
				break
			i += 1
			A[i] = A[j]
		return i + 1

s = Solution()
print s.removeDuplicates([1,1,1,2])