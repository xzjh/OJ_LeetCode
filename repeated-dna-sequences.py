class Solution:
	# @param s, a string
	# @return a list of strings
	def findRepeatedDnaSequences(self, s):
		d = {}
		for i in range(len(s) - 9):
			if s[i: i + 10] in d:
				d[s[i: i + 10]] += 1
			else:
				d[s[i: i + 10]] = 1
		res = []
		for (k, v) in d.iteritems():
			if v > 1:
				res.append(k)
				
		return res
