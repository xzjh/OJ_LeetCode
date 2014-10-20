class Solution:
	# @return a string
	def longestCommonPrefix(self, strs):
		if not strs:
			return ''

		flag = True
		i = 0
		for i in range(len(strs[0])):
			for j in range(1, len(strs)):
				if i >= len(strs[j]):
					i -= 1
					flag = False
					break
				flag = flag and strs[0][i] == strs[j][i]
				if not flag:
					i -= 1
					break
			if not flag:
				break
		return strs[0][:i + 1]

