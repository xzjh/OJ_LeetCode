class Solution:
	# @param s, a string
	# @return an integer
	def numDecodings(self, s):
		
		def helper(s, i):
			if i == len(s):
				return 1
			one = int(s[i:i + 1])
			two = int(s[i:i + 2])
			res = 0
			if one > 0 and one <= 26:
				if possible[i + 1] == -1:
					possible[i + 1] = helper(s, i + 1)
				res += possible[i + 1]
			if two != one and one > 0 and two > 0 and two <= 26:
				if possible[i + 2] == -1:
					possible[i + 2] = helper(s, i + 2)
				res += possible[i + 2]
			return res
		
		if not s:
			return 0
		possible = [-1] * (len(s) + 1)
		return helper(s, 0)
