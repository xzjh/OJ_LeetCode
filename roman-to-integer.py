class Solution:
	# @return an integer
	def romanToInt(self, s):
		if not s:
			return 0
		integer = [1000, 500, 100, 50, 10, 5, 1]
		roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
		level = len(roman) - 1
		res = 0
		for i in range(len(s))[::-1]:
			if s[i] in roman:
				idx = roman.index(s[i])
				if idx <= level:
					res += integer[idx]
					level = idx
				else:
					res -= integer[idx]
		return res