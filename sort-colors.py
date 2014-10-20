class Solution:
	# @param A a list of integers
	# @return nothing, sort in place
	def sortColors(self, A):
		if not A:
			return
		length = len(A)
		i = 0
		j = length - 1
		for k in [0, 1]:
			while i <= j:
				while i < length and A[i] == k:
					i += 1
				while j >= 0 and A[j] != k:
					j -= 1
				if i < length and j >= 0 and i < j:
					A[i], A[j] = A[j], A[i]
			j = length - 1

s = Solution()
A = [1,0]
s.sortColors(A)
print A