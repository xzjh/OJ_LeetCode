class Solution:
	# @param s, a string
	# @return an integer
	def titleToNumber(self, s):
		res = 0
		for d in s:
			res = res * 26 + ord(d) - ord('A') + 1
		return res
