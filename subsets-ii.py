class Solution:
	# @param num, a list of integer
	# @return a list of lists of integer
	def subsetsWithDup(self, S):
		
		def iter(s, res_item):
			if not s:
				res.append(res_item)
				return
			next_value_i = 1
			while next_value_i < len(s):
				if s[next_value_i] != s[0]:
					break
				next_value_i += 1
			iter(s[next_value_i:], res_item)
			iter(s[1:], res_item + [s[0]])
		
		res = []
		iter(sorted(S), [])
		return res
