class Solution:
	# @param s, a string
	# @param dict, a set of string
	# @return a list of strings
	def wordBreak(self, s, dict):
		
		def iter(start, r):
			if start >= len(s):
				res.append(r)
				return
			for i in range(start + 1, len(s) + 1):
				if s[start:i] in dd and possible[i]:
					nr = list(r)
					nr.append(s[start:i])
					res_len = len(res)
					iter(i, nr)
					if res_len == len(res):
						# not possible for this situation
						possible[i] = False

		dd = {}
		for w in dict:
			dd[w] = 1
		res = []
		possible = [True] * (len(s) + 1)
		iter(0, [])
		return map(' '.join, res)

s = Solution()
print s.wordBreak("a", ["b"])
