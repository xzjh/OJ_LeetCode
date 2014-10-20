class Solution:
	# @return a boolean
	def isMatch(self, s, p):

		def iter(s, p, ids, idp):
			if ids > len(s) - 1:
				return p[idp:] == '' or idp < len(p) - 1 and p[idp + 1:] == '*'
			if idp > len(p) - 1:
				return False

			if idp < len(p) - 1 and p[idp + 1] == '*':
				# print 1, ids,idp
				while ids < len(s) and (p[idp] == '.' or p[idp] == s[ids]):
					if iter(s, p, ids, idp + 2):
						return True
					ids += 1
				return iter(s, p, ids, idp + 2)
			else:
				# print 2,ids,idp
				return (p[idp] == '.' or p[idp] == s[ids]) and iter(s, p, ids + 1, idp + 1)

		return iter(s, p, 0, 0)

s = Solution()
print s.isMatch('','a*')