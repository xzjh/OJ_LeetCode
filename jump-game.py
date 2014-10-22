class Solution:
	# @param A, a list of integers
	# @return a boolean
	def canJump(self, A):
		last_good_node = len(A) - 1
		for i in range(len(A) - 1)[::-1]:
			if i + A[i] >= last_good_node:
				last_good_node = i
		return last_good_node == 0

s = Solution()
l =[3,2,1,0,4]
print s.canJump(l)
