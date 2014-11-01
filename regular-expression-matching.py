class Solution:
	# @return a boolean
	def isMatch(self, s, p):

		def iter(s, p, ids, idp):
			if idp > len(p) - 1:
				return ids == len(s)
			elif idp == len(p) - 1:
				# one char
				return ids == len(s) - 1 and (p[idp] == '.' or p[idp] == s[ids])
			else:
				if p[idp + 1] == '*':
					# print 1, ids,idp
					while ids < len(s) and (p[idp] == '.' or p[idp] == s[ids]):
						if possible[ids][idp + 2] and iter(s, p, ids, idp + 2):
							return True
						else:
							possible[ids][idp + 2] = False
						ids += 1
					if possible[ids][idp + 2] and iter(s, p, ids, idp + 2):
						return True
					else:
						possible[ids][idp + 2] = False
						return False
				else:
					# print 2,ids,idp
					if ids < len(s):
						if possible[ids + 1][idp + 1] and (p[idp] == '.' or p[idp] == s[ids]) and iter(s, p, ids + 1, idp + 1):
							return True
						else:
							possible[ids + 1][idp + 1] = False
							return False
					else:
						return False

		possible = [[True] * (len(p) + 1) for _ in range((len(s) + 1))]

		return iter(s, p, 0, 0)

s = Solution()
print s.isMatch("a", ".*.a*")
