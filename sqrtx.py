class Solution:
	# @param x, an integer
	# @return an integer
	def sqrt(self, x):
		if x < 0:
			return None
		elif x == 0:
			return 0
		r = 1
		high = 0
		low = 0
		while r * r <= x:
			r *= 2
		high = r
		low = r / 2

		if low * low == x:
			return low

		while high - low > 1:
			r = (high + low) / 2
			if r * r < x:
				low = r
			elif r * r > x:
				high = r
			else:
				return r

		return low

s = Solution()
print s.sqrt(9999)