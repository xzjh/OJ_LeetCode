class Solution:
	# @return an integer
	def lengthOfLongestSubstring(self, s):
		if not s:
			return 0
		d = {}
		length = len(s)
		i = 0
		start = 0
		res = 0
		while i < length:
			if s[i] in d:
				start = max(start, d[s[i]] + 1)
			d[s[i]] = i
			i += 1
			if res < i - start:
				res = i - start
		return res

s = Solution()
print s.lengthOfLongestSubstring("abcccccabc")
