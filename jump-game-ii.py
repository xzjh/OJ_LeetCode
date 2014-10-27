class Solution:
	# @param A, a list of integers
	# @return an integer
	def jump(self, A):
		length = len(A)
		if length == 1:
			return 0
		can_arrive = 0
		res = 0
		last_can_arrive = 0
		i = 0
		while can_arrive < length - 1:
			if i + A[i] > can_arrive:
				if i > last_can_arrive:
					last_can_arrive = can_arrive
					res += 1
				can_arrive = i + A[i]
			i += 1
		return res + 1

s = Solution()
l=[2,3,1,1,4]
print s.jump(l)