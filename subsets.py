class Solution:
	# @param S, a list of integer
	# @return a list of lists of integer
	def subsets(self, S):
		
		def iter(s, res_item):
			if not s:
				res.append(res_item)
				return
			iter(s[1:], res_item)
			iter(s[1:], res_item + [s[0]])
		
		res = []
		iter(sorted(S), [])
		return res
