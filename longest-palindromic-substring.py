class Solution:
	# @return a string
	def longestPalindrome(self, s):
		st = '#' + '#'.join(s) + '#'

		pal_len = 0
		pal_start = 0
		mx = 0
		idx = 0
		length = len(st)
		rad = [0] * length
		for i in range(1, length):
			if mx > i:
				rad[i] = min(rad[2 * idx - i], mx - i)
			else:
				rad[i] = 1
			while i + rad[i] < length and i - rad[i] >= 0 and \
				st[i + rad[i]] == st[i - rad[i]]:
				rad[i] += 1
			if rad[i] + i > mx:
				mx = rad[i] + i
				idx = i
			if pal_len < rad[i] - 1:
				pal_len = rad[i] - 1
				pal_start = (i - rad[i] + 1) / 2
		return s[pal_start: pal_start + pal_len]

s = Solution()
print s.longestPalindrome('abcdfghgfd213ww########')