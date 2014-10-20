class Solution:
	# @param A  a list of integers
	# @param m  an integer, length of A
	# @param B  a list of integers
	# @param n  an integer, length of B
	# @return nothing
	def merge(self, A, m, B, n):
		i = m - 1
		j = n - 1
		if i == -1:
			while j >= 0:
				A[j] = B[j]
				j -= 1
			return

		while i >= 0 and j >= 0:
			while i >= 0 and A[i] > B[j]:
				A[i + j + 1] = A[i]
				i -= 1
			while j >= 0 and (B[j] >= A[i] or i == -1):
				A[i + j + 1] = B[j]
				j -= 1

s = Solution()
A=[2,0]
s.merge(A,1,[1],1)
print A