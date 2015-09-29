class Solution(object):
	def nthUglyNumber(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		res = [1]
		if n == 1:
			return 1
		
		i1 = 0
		i2 = 0
		i3 = 0
		while len(res) < n:
			m2 = res[i1] * 2
			m3 = res[i2] * 3
			m5 = res[i3] * 5
			r = min(m2, m3, m5)
			if r == m2:
				i1 += 1
			if r == m3:
				i2 += 1
			if r == m5:
				i3 += 1
			res.append(r)
		
		return res[-1]
