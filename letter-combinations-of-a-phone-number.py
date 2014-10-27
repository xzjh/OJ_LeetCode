class Solution:
	# @return a list of strings, [s1, s2]
	def letterCombinations(self, digits):

		letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

		ans = ['']
		for d in digits:
			ans_t = []
			while ans:
				item = ans.pop(0)
				for c in letters[int(d)]:
					ans_t.append(item + c)
			ans.extend(ans_t)
		return ans

s = Solution()
print s.letterCombinations('23')