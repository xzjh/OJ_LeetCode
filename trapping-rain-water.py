class Solution:
	# @param A, a list of integers
	# @return an integer
	def trap(self, A):
		length = len(A)
		if length < 3:
			return 0
		left = [0] * length
		right = [0] * length
		ma = A[0]
		res = 0
		for i in range(1, length):
			if A[i] > ma:
				ma = A[i]
			left[i] = ma
		ma = A[-1]
		for i in range(0, length - 1)[::-1]:
			if A[i] > ma:
				ma = A[i]
			right[i] = ma
			t = min(left[i], right[i]) - A[i]
			if t > 0:
				res += t

		return res

s = Solution()
print s.trap([4,2,3])