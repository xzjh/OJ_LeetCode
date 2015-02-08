class Solution:
	# @return a float
	def findMedianSortedArrays(self, A, B):

		def getKthNum(A, B, k):
			len_A = len(A)
			len_B = len(B)
			if len_A == 0:
				return B[k - 1]
			if len_B == 0:
				return A[k - 1]
			if k == 1:
				return min(A[0], B[0])
			if len_A / 2 + len_B / 2 + 1 >= k:
				if A[len_A / 2] > B[len_B / 2]:
					return getKthNum(A[:len_A / 2], B, k)
				else:
					return getKthNum(A, B[: len_B / 2], k)
			else:
				if A[len_A / 2] > B[len_B / 2]:
					return getKthNum(A, B[len_B / 2 + 1:], k - (len_B / 2 + 1))
				else:
					return getKthNum(A[len_A / 2 + 1:], B, k - (len_A / 2 + 1))

		len_A = len(A)
		len_B = len(B)
		if (len_A + len_B) % 2 == 0:
			return (getKthNum(A, B, (len_A + len_B) / 2) + getKthNum(A, B, (len_A + len_B) / 2 + 1)) / 2.0
		else:
			return getKthNum(A, B, (len_A + len_B) / 2 + 1)

s = Solution()
print s.findMedianSortedArrays([1,2], [1,2])
