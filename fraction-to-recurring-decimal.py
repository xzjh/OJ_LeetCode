class Solution:
	# @return a string
	def fractionToDecimal(self, numerator, denominator):
		sign = ''
		if numerator > 0 and denominator < 0:
			denominator = -denominator
			sign = '-'
		elif numerator < 0 and denominator > 0:
			numerator = -numerator
			sign = '-'

		integer = numerator // denominator
		remaining = numerator % denominator
		d = {}
		res = ''
		p = 0
		while remaining:
			remaining *= 10
			if remaining in d:
				res = res[:d[remaining]] + '(' + res[d[remaining]:] + ')'
				break
			else:
				d[remaining] = p
			q = remaining // denominator
			remaining %= denominator
			res += str(q)
			p += 1
		if res == '':
			return sign + str(integer)
		else:
			return sign + str(integer) + '.' + res

s = Solution()
print s.fractionToDecimal(1, 333)