class Solution:
	# @return a string
	def convert(self, s, nRows):
		if not s or nRows <= 1:
			return s
		res = ''
		for si in range(nRows):
			for i in range(si, len(s))[::2 * nRows - 2]:
				res += s[i]
				if si > 0 and si < nRows - 1 and i - 2 * si + 2 * nRows - 2 < len(s):
					res += s[i - 2 * si + 2 * nRows - 2]
		return res

s = Solution()
print s.convert('ABCDEF', 1)