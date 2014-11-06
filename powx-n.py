class Solution:
	# @param x, a float
	# @param n, a integer
	# @return a float
	def pow(self, x, n):
		if n == 0:
			return float(1.0)
		elif n > 0:
			res = pow(x, n // 2)
			if n % 2 == 0:
				return res * res
			else:
				return res * res * x
		else:
			return float(1.0) / pow(x, -n)
