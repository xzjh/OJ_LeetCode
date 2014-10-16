class Solution:
	# @return an integer
	def reverse(self, x):
		s = 1
		if x < 0:
			s = -1
			x = -x
		return s * int(str(x)[::-1])