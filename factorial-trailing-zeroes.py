class Solution:
	# @return an integer
	def trailingZeroes(self, n):
		
		res = 0
		d = 5
		t = n // d
		while t >= 1:
			res += t
			d *= 5
			t = n // d
		return res
