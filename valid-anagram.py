class Solution:
	# @param {string} s
	# @param {string} t
	# @return {boolean}
	def isAnagram(self, s, t):
		return ''.join(sorted(s)) == ''.join(sorted(t))
