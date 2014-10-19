class Solution:
	# @param    A       a list of integers
	# @param    elem    an integer, value need to be removed
	# @return an integer
	def removeElement(self, A, elem):
		length = len(A)
		if length == 0:
			return 0
		i = 0
		j = length - 1
		while i <= j:
			while i < length and A[i] != elem:
				i += 1
			while j >= 0 and A[j] == elem:
				j -= 1
				length -= 1
			if i < j:
				A[i], A[j] = A[j], A[i]
				i += 1
				j -= 1
				length -= 1
		return length

s = Solution()
print s.removeElement([2], 3)