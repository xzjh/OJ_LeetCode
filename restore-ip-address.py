class Solution:
	# @param s, a string
	# @return a list of strings
	def restoreIpAddresses(self, s):
		
		def iter(s, n, ans, sol):
			l = len(s)
			if l == 0:
				return
			if n == 0:
				v = int(s)
				if v >= 0 and v <= 255 and (l == 1 or s[0] != '0'):
					ans += s
					sol.append(ans)
				return

			if l == 1:
				return
			if l > 1:
				iter(s[1:], n - 1, ans + s[:1] + '.', sol)
			if l > 2 and s[0] != '0':
					iter(s[2:], n - 1, ans + s[:2] + '.', sol)
			if l > 3 and s[0] != '0':
				v = int(s[:3])
				if v >= 0 and v <= 255:
					iter(s[3:], n - 1, ans + s[:3] + '.', sol)

		if not s:
			return []

		sol = []
		iter(s, 3, '', sol)
		return sol

s = Solution()
print s.restoreIpAddresses("010010")