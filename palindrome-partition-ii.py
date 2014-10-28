class Solution:
	# @param s, a string
	# @return an integer
	def minCut(self, s):
		length = len(s)
		is_pal = [[False] * length for _ in range(length)]
		min_cut = [0] * (length + 1)
		for i in range(length + 1):
			min_cut[i] = length - i - 1
		for i in range(length)[::-1]:
			for j in range(i, length):
				if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
					is_pal[i][j] = True
					min_cut[i] = min(min_cut[i], min_cut[j + 1] + 1)
		return min_cut[0]

s = Solution()
print s.minCut('bb')