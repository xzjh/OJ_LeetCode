class Solution:
	# @return an integer
	def divide(self, dividend, divisor):
		
		sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
		if dividend < 0:
			dividend = -dividend
		if divisor < 0:
			divisor = -divisor
		ans = 0
		while dividend >= divisor:
			a = divisor
			t = 0
			while a <= dividend:
				a <<= 1
				t += 1
			ans += 1 << (t - 1)
			dividend -= a >> 1
		return sign * ans

s = Solution()
print s.divide(100,3)