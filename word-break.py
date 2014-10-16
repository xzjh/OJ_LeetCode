class Solution:
	# @param s, a string
	# @param dict, a set of string
	# @return a boolean
	def wordBreak(self, s, dict):
		if len(s) == 0 or len(dict) == 0:
			return False

		dd = {}
		ok = [False] * (len(s) + 1)
		ok[0] = True
		for word in dict:
			dd[word] = 1
		for i in range(1, len(s) + 1):
			for j in range(i):
				if dd.has_key(s[j:i]) and ok[j]:
					ok[i] = True
					break

		return ok[len(s)]

s = Solution()
d = ['leet','code']
st = 'leetcodes'
print s.wordBreak(st, d)