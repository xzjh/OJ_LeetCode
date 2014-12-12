class Solution:
	# @param A a list of integers
	# @return an integer
	def removeDuplicates(self, A):
		if not A:
			return 0
		if len(A) <= 1:
			return len(A)
		left = 0
		dup = 1
		right = 1
		while right < len(A):
			if A[right] == A[right - 1]:
				dup += 1
			else:
				dup = 1
			if A[left] == A[right] and dup > 2:
				while right < len(A) and A[right] == A[right - 1]:
					right += 1
				dup = 0
			else:
				left += 1
				A[left] = A[right]
				right += 1
		return left + 1
